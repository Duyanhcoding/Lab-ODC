import 'package:flutter/material.dart';
import '../talent/talent_home.dart'; // Import dashboard của Talent
import '../enterprise/enterprise_home.dart';
import '../mentor/mentor_home.dart';
import '../admin/admin_home.dart';

class RoleSelectionScreen extends StatelessWidget {
  final String email;
  const RoleSelectionScreen({super.key, required this.email});

  void _goToRole(BuildContext context, String role) {
    final userData = {'user': {'email': email, 'role': role}};

    Widget screen;
    switch (role) {
      case 'enterprise': screen = EnterpriseHomeScreen(userData: userData); break;
      case 'mentor': screen = MentorHomeScreen(userData: userData); break;
      case 'admin': screen = AdminHomeScreen(userData: userData); break;
      default: screen = TalentHomeScreen(userData: userData); // Vào Talent Dashboard
    }

    // --- SỬA ĐỔI QUAN TRỌNG Ở ĐÂY ---
    // Dùng push (thay vì pushReplacement) để CHỒNG màn hình Role lên trên.
    // Khi bấm Back ở màn hình Role, nó sẽ gỡ màn hình Role ra -> Lộ ra màn hình Chọn Role bên dưới.
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => screen),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Chọn Vai Trò")),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          const Text("Vui lòng chọn vai trò để tiếp tục:", style: TextStyle(fontSize: 16, color: Colors.grey)),
          const SizedBox(height: 20),
          _buildCard(context, "Ứng Viên (Talent)", Icons.person, Colors.green, 'talent'),
          _buildCard(context, "Doanh Nghiệp", Icons.business, Colors.blue, 'enterprise'),
          _buildCard(context, "Mentor / Giảng Viên", Icons.school, Colors.orange, 'mentor'),
          _buildCard(context, "Quản Trị Viên (Admin)", Icons.admin_panel_settings, Colors.red, 'admin'),
        ],
      ),
    );
  }

  Widget _buildCard(BuildContext context, String title, IconData icon, Color color, String roleKey) {
    return Card(
      margin: const EdgeInsets.only(bottom: 15),
      child: ListTile(
        leading: CircleAvatar(backgroundColor: color.withOpacity(0.2), child: Icon(icon, color: color)),
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        trailing: const Icon(Icons.arrow_forward_ios, size: 16),
        onTap: () => _goToRole(context, roleKey),
      ),
    );
  }
}