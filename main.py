import os
import winreg
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import re

class MACChangerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MAC Address Changer - Hoathinh2d.com - Công cụ đổi địa chỉ MAC")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Tạo style cho giao diện
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.adapters = []
        self.selected_adapter = None
        
        self.create_widgets()
        self.load_adapters()
        
    def create_widgets(self):
        # Frame chính
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Cấu hình grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Tiêu đề
        title_label = ttk.Label(main_frame, text="🔧 MAC Address Changer", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Khung danh sách card mạng
        adapter_frame = ttk.LabelFrame(main_frame, text="📡 Danh sách Card mạng", padding="10")
        adapter_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        adapter_frame.columnconfigure(0, weight=1)
        adapter_frame.rowconfigure(1, weight=1)
        
        # Nút refresh
        refresh_btn = ttk.Button(adapter_frame, text="🔄 Làm mới danh sách", 
                                command=self.load_adapters)
        refresh_btn.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        # Treeview cho danh sách adapter
        columns = ('key', 'name')
        self.adapter_tree = ttk.Treeview(adapter_frame, columns=columns, show='headings', height=8)
        self.adapter_tree.heading('key', text='Key')
        self.adapter_tree.heading('name', text='Tên Card mạng')
        self.adapter_tree.column('key', width=100)
        self.adapter_tree.column('name', width=400)
        
        # Scrollbar cho treeview
        scrollbar = ttk.Scrollbar(adapter_frame, orient=tk.VERTICAL, command=self.adapter_tree.yview)
        self.adapter_tree.configure(yscrollcommand=scrollbar.set)
        
        self.adapter_tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        
        # Bind event
        self.adapter_tree.bind('<<TreeviewSelect>>', self.on_adapter_select)
        
        # Khung nhập MAC
        mac_frame = ttk.LabelFrame(main_frame, text="🔧 Thay đổi MAC Address", padding="10")
        mac_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        mac_frame.columnconfigure(1, weight=1)
        
        # Label và Entry cho MAC
        ttk.Label(mac_frame, text="MAC Address mới:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.mac_entry = ttk.Entry(mac_frame, font=('Courier', 12))
        self.mac_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        self.mac_entry.bind('<KeyRelease>', self.validate_mac)
        
        # Nút thay đổi
        self.change_btn = ttk.Button(mac_frame, text="🔄 Thay đổi MAC", 
                                    command=self.change_mac, state='disabled')
        self.change_btn.grid(row=0, column=2)
        
        # Hướng dẫn
        help_text = ("💡 Hướng dẫn:\n"
                    "1. Chọn card mạng từ danh sách trên\n"
                    "2. Nhập MAC address mới (12 ký tự hex, ví dụ: 001122334455)\n"
                    "3. Nhấn 'Thay đổi MAC' để áp dụng\n"
                    "4. Card mạng sẽ tự động khởi động lại\n\n"
                    "⚠️ Lưu ý: Cần chạy với quyền Administrator")
        
        help_frame = ttk.LabelFrame(main_frame, text="📋 Hướng dẫn sử dụng", padding="10")
        help_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        help_frame.columnconfigure(0, weight=1)
        
        help_label = ttk.Label(help_frame, text=help_text, justify=tk.LEFT)
        help_label.grid(row=0, column=0, sticky=tk.W)
        
        # Khung log
        log_frame = ttk.LabelFrame(main_frame, text="📄 Nhật ký hoạt động", padding="10")
        log_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=8, state='disabled')
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Cấu hình grid weights
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
    def log_message(self, message):
        """Ghi log vào text widget"""
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')
        self.root.update()
        
    def validate_mac(self, event=None):
        """Kiểm tra định dạng MAC address"""
        mac = self.mac_entry.get().strip().replace(':', '').replace('-', '').upper()
        
        # Tự động format
        if len(mac) <= 12:
            self.mac_entry.delete(0, tk.END)
            self.mac_entry.insert(0, mac)
        
        # Kiểm tra định dạng
        is_valid = len(mac) == 12 and re.match(r'^[0-9A-F]{12}$', mac)
        
        if is_valid and self.selected_adapter:
            self.change_btn.config(state='normal')
        else:
            self.change_btn.config(state='disabled')
            
        return is_valid
    
    def list_network_adapters(self):
        """Lấy danh sách card mạng từ registry"""
        base_key_path = r"SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}"
        adapters = []
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, base_key_path) as base_key:
                i = 0
                while True:
                    try:
                        subkey_name = winreg.EnumKey(base_key, i)
                        with winreg.OpenKey(base_key, subkey_name) as subkey:
                            try:
                                name, _ = winreg.QueryValueEx(subkey, "DriverDesc")
                                adapters.append((subkey_name, name))
                            except FileNotFoundError:
                                pass
                        i += 1
                    except OSError:
                        break
        except Exception as e:
            self.log_message(f"❌ Lỗi truy cập registry: {e}")
        
        return adapters
    
    def load_adapters(self):
        """Tải danh sách card mạng vào giao diện"""
        self.log_message("🔍 Đang tải danh sách card mạng...")
        
        # Xóa dữ liệu cũ
        for item in self.adapter_tree.get_children():
            self.adapter_tree.delete(item)
            
        # Tải dữ liệu mới
        self.adapters = self.list_network_adapters()
        
        if not self.adapters:
            self.log_message("⚠️ Không tìm thấy card mạng nào hoặc thiếu quyền truy cập")
            return
            
        for key, name in self.adapters:
            self.adapter_tree.insert('', 'end', values=(key, name))
            
        self.log_message(f"✅ Đã tải {len(self.adapters)} card mạng")
    
    def on_adapter_select(self, event):
        """Xử lý khi chọn adapter"""
        selection = self.adapter_tree.selection()
        if selection:
            item = self.adapter_tree.item(selection[0])
            values = item['values']
            self.selected_adapter = (values[0], values[1])
            self.log_message(f"📡 Đã chọn: {values[1]}")
            self.validate_mac()
    
    def set_mac_address(self, adapter_key, new_mac):
        """Thay đổi MAC address trong registry"""
        base_key_path = r"SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}"
        full_key = base_key_path + "\\" + adapter_key
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, full_key, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "NetworkAddress", 0, winreg.REG_SZ, new_mac)
            self.log_message(f"✅ Đã đổi MAC thành: {new_mac}")
            return True
        except Exception as e:
            self.log_message(f"❌ Lỗi khi đổi MAC: {e}")
            return False
    
    def restart_adapter(self, adapter_name):
        """Khởi động lại card mạng"""
        try:
            self.log_message("🔁 Đang khởi động lại card mạng...")
            
            # Tắt adapter
            result1 = subprocess.run(f'netsh interface set interface "{adapter_name}" admin=disable', 
                                   shell=True, capture_output=True, text=True)
            
            # Bật adapter
            result2 = subprocess.run(f'netsh interface set interface "{adapter_name}" admin=enable', 
                                   shell=True, capture_output=True, text=True)
            
            if result1.returncode == 0 and result2.returncode == 0:
                self.log_message("✅ Đã khởi động lại card mạng thành công")
                return True
            else:
                self.log_message(f"❌ Lỗi khởi động lại: {result1.stderr or result2.stderr}")
                return False
                
        except Exception as e:
            self.log_message(f"❌ Lỗi khởi động lại card mạng: {e}")
            return False
    
    def change_mac_worker(self):
        """Worker thread để thay đổi MAC"""
        try:
            new_mac = self.mac_entry.get().strip().replace(':', '').replace('-', '').upper()
            key, name = self.selected_adapter
            
            self.log_message(f"🔧 Bắt đầu thay đổi MAC cho: {name}")
            
            # Thay đổi MAC
            if self.set_mac_address(key, new_mac):
                # Khởi động lại adapter
                if self.restart_adapter(name):
                    self.log_message("🎉 Thay đổi MAC address thành công!")
                    messagebox.showinfo("Thành công", "Đã thay đổi MAC address thành công!")
                else:
                    messagebox.showwarning("Cảnh báo", "Đã thay đổi MAC nhưng không thể khởi động lại card mạng. Vui lòng khởi động lại thủ công.")
            else:
                messagebox.showerror("Lỗi", "Không thể thay đổi MAC address. Kiểm tra quyền Administrator.")
                
        except Exception as e:
            self.log_message(f"❌ Lỗi: {e}")
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")
        finally:
            self.change_btn.config(state='normal')
    
    def change_mac(self):
        """Thay đổi MAC address"""
        if not self.selected_adapter:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn card mạng!")
            return
            
        new_mac = self.mac_entry.get().strip().replace(':', '').replace('-', '').upper()
        if not self.validate_mac():
            messagebox.showwarning("Cảnh báo", "MAC address không hợp lệ! Vui lòng nhập 12 ký tự hex.")
            return
        
        # Xác nhận
        result = messagebox.askyesno("Xác nhận", 
                                   f"Bạn có chắc muốn đổi MAC của '{self.selected_adapter[1]}' thành '{new_mac}'?\n\n"
                                   "Card mạng sẽ bị ngắt kết nối tạm thời.")
        
        if result:
            self.change_btn.config(state='disabled')
            # Chạy trong thread riêng để không block GUI
            thread = threading.Thread(target=self.change_mac_worker, daemon=True)
            thread.start()

def main():
    # Kiểm tra quyền admin
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    root = tk.Tk()
    
    if not is_admin:
        messagebox.showwarning("Cảnh báo", 
                             "Ứng dụng cần chạy với quyền Administrator để thay đổi MAC address.\n"
                             "Vui lòng chạy lại với quyền Administrator.")
    
    app = MACChangerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()