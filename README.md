# Change-Mac-Address
MAC Address Changer - Công cụ đổi địa chỉ MAC - Tô Đình Duy
🔧 MAC Address Changer - Tài liệu hướng dẫn toàn diện
📋 Mục lục

Giới thiệu
Yêu cầu hệ thống
Cài đặt và thiết lập
Hướng dẫn sử dụng
Tính năng chi tiết
Xử lý sự cố
FAQ - Câu hỏi thường gặp
Lưu ý bảo mật và pháp lý
Kỹ thuật chi tiết
Changelog


🎯 Giới thiệu
MAC Address Changer là một công cụ đồ họa mạnh mẽ được thiết kế để thay đổi địa chỉ MAC (Media Access Control) của các card mạng trên hệ điều hành Windows. Công cụ này cung cấp giao diện người dùng trực quan, dễ sử dụng và các tính năng an toàn để quản lý danh tính mạng của thiết bị.
🌟 Tại sao cần thay đổi MAC Address?

Bảo mật và riêng tư: Ngăn chặn việc theo dõi thiết bị qua địa chỉ MAC
Bypass MAC filtering: Vượt qua các hạn chế mạng dựa trên MAC address
Network testing: Kiểm tra cấu hình mạng và bảo mật
Device management: Quản lý nhiều thiết bị trong môi trường doanh nghiệp
Troubleshooting: Giải quyết các vấn đề kết nối mạng

✨ Ưu điểm nổi bật

Giao diện đồ họa hiện đại: Dễ sử dụng, không cần command line
Validation tự động: Kiểm tra định dạng MAC address real-time
Logging chi tiết: Theo dõi toàn bộ quá trình thực hiện
Multi-threading: Không block giao diện khi thực hiện tác vụ
Safety features: Xác nhận trước khi thực hiện thay đổi
Cross-adapter support: Hỗ trợ tất cả loại card mạng


💻 Yêu cầu hệ thống
Hệ điều hành

Windows 7 trở lên (khuyến nghị Windows 10/11)
Architecture: x86 hoặc x64

Phần mềm

Python 3.6+ (khuyến nghị Python 3.8 trở lên)
Tkinter (thường có sẵn với Python)
Administrator privileges (bắt buộc)

Phần cứng

RAM: Tối thiểu 512MB
Storage: 10MB trống
Network adapter: Ít nhất 1 card mạng

Dependencies
python# Các thư viện cần thiết (có sẵn trong Python standard library)
import os
import winreg
import subprocess
import tkinter
import threading
import re

🚀 Cài đặt và thiết lập
Bước 1: Chuẩn bị môi trường

Kiểm tra Python:
cmdpython --version
Nếu chưa có Python, tải từ python.org
Kiểm tra Tkinter:
cmdpython -c "import tkinter; print('Tkinter OK')"


Bước 2: Tải và cài đặt

Tạo thư mục dự án:
cmdmkdir MAC_Changer
cd MAC_Changer

Lưu source code vào file mac_changer_gui.py
Tạo shortcut với quyền Admin:

Chuột phải vào file Python
Chọn "Create shortcut"
Chuột phải vào shortcut → Properties
Advanced → "Run as administrator"



Bước 3: Chạy ứng dụng
cmd# Cách 1: Chạy trực tiếp (cần mở Command Prompt as Administrator)
python mac_changer_gui.py

# Cách 2: Sử dụng shortcut đã tạo
# Double-click vào shortcut

📖 Hướng dẫn sử dụng
Khởi động ứng dụng

Chạy với quyền Administrator (bắt buộc)
Giao diện chính sẽ hiển thị với các phần:

Danh sách card mạng
Ô nhập MAC address mới
Hướng dẫn sử dụng
Nhật ký hoạt động



Quy trình thay đổi MAC
Bước 1: Chọn card mạng
Show Image

Xem danh sách các card mạng trong bảng
Click vào card mạng muốn thay đổi
Thông tin card được chọn sẽ hiển thị trong log

Bước 2: Nhập MAC address mới
Show Image

Nhập MAC address mới vào ô text
Định dạng hỗ trợ:

001122334455 (12 ký tự liên tiếp)
00:11:22:33:44:55 (có dấu hai chấm)
00-11-22-33-44-55 (có dấu gạch ngang)


Validation tự động:

Ký tự không hợp lệ sẽ bị loại bỏ
Nút "Thay đổi MAC" chỉ active khi MAC hợp lệ



Bước 3: Thực hiện thay đổi
Show Image

Click nút "🔄 Thay đổi MAC"
Xác nhận trong dialog popup
Theo dõi tiến trình trong phần log:

Thay đổi registry
Restart card mạng
Thông báo kết quả



Thao tác bổ sung
Làm mới danh sách

Click "🔄 Làm mới danh sách" để reload các card mạng
Hữu ích khi có thay đổi phần cứng

Theo dõi log

Tất cả hoạt động được ghi trong phần "Nhật ký hoạt động"
Scroll để xem lịch sử đầy đủ
Log bao gồm timestamp và trạng thái


🛠️ Tính năng chi tiết
1. Quản lý Card mạng
Phát hiện tự động

Quét registry Windows để tìm tất cả network adapters
Hiển thị cả tên hiển thị và registry key
Hỗ trợ tất cả loại card: Ethernet, WiFi, Virtual

Thông tin chi tiết
Key: 0001          | Tên: Intel(R) Ethernet Connection
Key: 0002          | Tên: Realtek PCIe GbE Family Controller
Key: 0003          | Tên: Microsoft Wi-Fi Direct Virtual Adapter
2. Validation MAC Address
Định dạng hỗ trợ

Hex only: 001122334455
Colon separated: 00:11:22:33:44:55
Dash separated: 00-11-22-33-44-55
Mixed case: Tự động convert thành uppercase

Kiểm tra real-time

Validation khi người dùng nhập
Loại bỏ ký tự không hợp lệ
Visual feedback qua enable/disable button

Ký tự hợp lệ
Allowed: 0-9, A-F, a-f, :, -
Invalid: G-Z, special characters, spaces
Length: Exactly 12 hex characters
3. Registry Operations
Read Operations

Truy cập HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}
Enum tất cả subkeys
Đọc DriverDesc để lấy tên card

Write Operations

Set NetworkAddress value trong registry
Sử dụng REG_SZ data type
Atomic operations với proper error handling

4. Network Restart
Disable/Enable Sequence
cmdnetsh interface set interface "Adapter Name" admin=disable
netsh interface set interface "Adapter Name" admin=enable
Timing và Synchronization

Sequential execution
Error checking cho mỗi bước
User feedback trong real-time

5. GUI Features
Threading Model

Main thread cho GUI operations
Worker threads cho network operations
Thread-safe logging mechanism

User Experience

Progress indication
Confirmation dialogs
Error messages với suggestions
Responsive design


🔧 Xử lý sự cố
Lỗi thường gặp
1. "Access Denied" hoặc "Permission Error"
Nguyên nhân: Thiếu quyền Administrator
Giải pháp:

Đảm bảo chạy Python/CMD với "Run as Administrator"
Kiểm tra UAC settings
Tạo shortcut với quyền admin

2. "Card mạng không khởi động lại"
Nguyên nhân:

Driver không hỗ trợ
Card đang được sử dụng bởi ứng dụng khác

Giải pháp:
cmd# Manual restart
netsh interface show interface
netsh interface set interface "Interface Name" admin=disable
netsh interface set interface "Interface Name" admin=enable

# Hoặc từ Device Manager
devmgmt.msc → Network adapters → Disable/Enable
3. "Không tìm thấy card mạng"
Nguyên nhân: Registry access issues
Giải pháp:

Kiểm tra Windows services: services.msc
Restart "Plug and Play" service
Scan for hardware changes trong Device Manager

4. "MAC không thay đổi"
Nguyên nhân:

Driver lock
Hardware limitation

Giải pháp:

Kiểm tra trong Device Manager → Properties → Advanced
Tìm "Network Address" hoặc "Locally Administered Address"
Một số card không hỗ trợ MAC spoofing

Debug Steps
1. Kiểm tra Registry
cmdregedit
# Navigate to: HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}
# Look for "NetworkAddress" values
2. Kiểm tra Network Interfaces
cmdipconfig /all
netsh interface show interface
getmac /v
3. Event Viewer
Windows Logs → System
Look for network adapter events
Filter by Event ID: 20, 27, 32
Recovery Procedures
Khôi phục MAC gốc

Registry method:

Delete NetworkAddress value
Restart adapter


Device Manager method:

Properties → Advanced → Network Address
Set to "Not Present" hoặc empty


Factory reset:

Uninstall driver
Scan for hardware changes




❓ FAQ - Câu hỏi thường gặp
Q1: MAC address có bị mất khi restart máy?
A: Không, thay đổi được lưu trong registry và persist qua restart. Để khôi phục MAC gốc, cần xóa value NetworkAddress trong registry.
Q2: Có thể thay đổi MAC của tất cả card mạng?
A: Hầu hết các card mạng hiện đại đều hỗ trợ. Một số card onboard hoặc cũ có thể không hỗ trợ. Virtual adapters thường hỗ trợ tốt.
Q3: Có an toàn khi thay đổi MAC address?
A: Có, đây là tính năng được Windows hỗ trợ chính thức. Tuy nhiên nên backup MAC gốc và test trước khi sử dụng trong production.
Q4: Tại sao cần quyền Administrator?
A: Vì cần truy cập và chỉnh sửa registry của hệ thống, cụ thể là HKEY_LOCAL_MACHINE. Đây là vùng registry được bảo vệ.
Q5: Có thể tự động hóa quá trình này?
A: Có, có thể tạo script batch hoặc PowerShell để tự động thay đổi MAC theo lịch trình.
Q6: MAC giả có bị phát hiện không?
A: Thông thường không, vì MAC chỉ hoạt động ở layer 2 (data link). Tuy nhiên một số tool chuyên dụng có thể phát hiện.
Q7: Có ảnh hưởng đến hiệu suất mạng?
A: Không, MAC address chỉ là identifier, không ảnh hưởng đến băng thông hay latency.

🔒 Lưu ý bảo mật và pháp lý
Sử dụng hợp pháp
✅ Các mục đích được khuyến khích:

Network testing và penetration testing (với permission)
Privacy protection trong mạng công cộng
Device management trong doanh nghiệp
Research và education
Troubleshooting network issues

❌ Tránh sử dụng cho:

Bypass security systems trái phép
Hide malicious activities
Violate terms of service của ISP
Impersonate other devices không có permission

Best Practices
Security Guidelines

Backup MAC gốc trước khi thay đổi
Test trong môi trường lab trước khi production
Document changes để tracking
Use strong new MAC (avoid common patterns)
Monitor network behavior sau khi thay đổi

Legal Compliance

Tuân thủ local laws và regulations
Respect corporate policies
Obtain proper authorization khi cần
Don't violate network terms of service
Be transparent về mục đích sử dụng

Risk Assessment
Low Risk:

Personal device trên personal network
Testing environment
Educational purposes

Medium Risk:

Corporate network (cần approval)
Public WiFi (check ToS)
Shared network environments

High Risk:

ISP network manipulation
Critical infrastructure
Unauthorized access attempts


⚙️ Kỹ thuật chi tiết
Architecture Overview
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   GUI Layer     │    │  Business Logic │    │   System Layer  │
│                 │    │                 │    │                 │
│ • Tkinter UI    │◄──►│ • Validation    │◄──►│ • Registry API  │
│ • Event Handling│    │ • MAC Formatting│    │ • Network CMD   │
│ • User Input    │    │ • Error Handling│    │ • Process Mgmt  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
Registry Structure
HKEY_LOCAL_MACHINE\
└── SYSTEM\
    └── CurrentControlSet\
        └── Control\
            └── Class\
                └── {4D36E972-E325-11CE-BFC1-08002BE10318}\  # Network adapters GUID
                    ├── 0000\                                 # First adapter
                    │   ├── DriverDesc = "Intel Ethernet"
                    │   ├── NetworkAddress = "001122334455"   # Our modification
                    │   └── ...
                    ├── 0001\                                 # Second adapter
                    └── ...
Threading Model
pythonMain Thread (GUI):
├── UI Rendering
├── Event Handling
└── User Interaction

Worker Thread:
├── Registry Operations
├── Network Commands
└── Progress Updates → Main Thread
Error Handling Strategy
pythontry:
    # Registry operation
    registry_operation()
except PermissionError:
    # Handle admin rights issue
except FileNotFoundError:
    # Handle missing registry key
except Exception as e:
    # Generic error handling
    log_error(e)
    show_user_friendly_message()
MAC Address Validation
pythondef validate_mac(mac_string):
    # Remove separators
    clean_mac = re.sub(r'[:-]', '', mac_string.upper())
    
    # Check length and hex characters
    pattern = r'^[0-9A-F]{12}$'
    return re.match(pattern, clean_mac) is not None
Network Interface Management
cmd# Detection
netsh interface show interface

# Status check
netsh interface show interface "Interface Name"

# Administrative control
netsh interface set interface "Interface Name" admin=disable
netsh interface set interface "Interface Name" admin=enable

📊 Performance và Monitoring
Performance Metrics
Typical Operations Timing:

Registry scan: 100-500ms
MAC validation: <1ms
Registry write: 10-50ms
Network restart: 2-10 seconds
GUI responsiveness: Real-time

Memory Usage:

Base application: ~5-10MB
Peak usage: ~15-20MB
Thread overhead: ~1-2MB per worker

Monitoring Tools
Built-in Logging
python# Log levels implemented:
INFO:  Normal operations
WARN:  Non-critical issues  
ERROR: Failed operations
DEBUG: Detailed troubleshooting
External Monitoring
cmd# Windows Performance Monitor
perfmon

# Network monitoring
netstat -an
netsh interface show interface

# Registry monitoring
procmon (Process Monitor)

🔄 Changelog
Version 1.0.0 (Current)
Release Date: 2024
🎉 New Features:

Giao diện đồ họa đầy đủ với tkinter
Auto-detection tất cả network adapters
Real-time MAC address validation
Multi-threading support
Comprehensive logging system
User-friendly error messages
Administrator privilege checking

🛠️ Technical Improvements:

Registry-based MAC address modification
Proper error handling và recovery
Thread-safe GUI operations
Modular code architecture
Cross-adapter compatibility

🔒 Security Enhancements:

Permission validation
User confirmation dialogs
Safe registry operations
Process isolation

Planned Features (Future Versions):
Version 1.1.0:

 MAC address history và favorites
 Batch operations cho multiple adapters
 Export/Import configuration
 Scheduled MAC rotation

Version 1.2.0:

 Advanced filtering options
 Network adapter statistics
 Integration với Windows notifications
 Command-line interface option

Version 2.0.0:

 Support cho Linux/macOS
 Web-based interface
 REST API endpoints
 Plugin architecture


📞 Hỗ trợ và liên hệ
Troubleshooting Resources

Built-in Help: Sử dụng hướng dẫn trong ứng dụng
Log Analysis: Kiểm tra phần "Nhật ký hoạt động"
Windows Event Viewer: Tìm network-related events
Device Manager: Verify adapter status

Best Practices cho Support

Collect logs từ ứng dụng
Note exact error messages
Include system information (Windows version, Python version)
Describe steps to reproduce issue
Check permissions và admin rights

Contributing Guidelines

Report bugs với detailed information
Suggest features với use cases
Follow coding standards
Include tests cho new features
Update documentation khi cần


📝 Kết luận
MAC Address Changer là một công cụ mạnh mẽ và an toàn để quản lý địa chỉ MAC trên Windows. Với giao diện trực quan, tính năng validation mạnh mẽ, và logging chi tiết, đây là giải pháp ideal cho các mục đích testing, privacy, và network management.
Key Takeaways:

Easy to use: Giao diện đồ họa thân thiện
Safe operations: Validation và confirmation dialogs
Comprehensive logging: Theo dõi đầy đủ quá trình
Professional grade: Suitable cho enterprise use
Well documented: Hướng dẫn chi tiết và troubleshooting

Recommended Usage:

Start với testing trên máy không quan trọng
Backup MAC addresses gốc
Follow best practices về security
Monitor network behavior sau khi thay đổi
Keep documentation về changes made
