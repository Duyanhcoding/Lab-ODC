import 'package:flutter/material.dart';
import '../auth/login_screen.dart';

class MentorHomeScreen extends StatelessWidget {
  final Map<String, dynamic> userData;
  const MentorHomeScreen({super.key, required this.userData});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Không gian Mentor"),
        backgroundColor: Colors.purple,
        foregroundColor: Colors.white,
        actions: [IconButton(onPressed: () => Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const LoginScreen())), icon: const Icon(Icons.logout))],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            const TextField(
              decoration: InputDecoration(prefixIcon: Icon(Icons.search), hintText: "Tìm kiếm sinh viên...", border: OutlineInputBorder()),
            ),
            const SizedBox(height: 20),
            Expanded(
              child: ListView(
                children: [
                  _buildStudentItem("Nguyễn Văn A", "Dự án: App Mobile", 0.8),
                  _buildStudentItem("Trần Thị B", "Dự án: Website Bán Hàng", 0.4),
                  _buildStudentItem("Lê Văn C", "Dự án: AI Chatbot", 0.1),
                  _buildStudentItem("Phạm Minh D", "Dự án: IoT Garden", 0.9),
                ],
              ),
            )
          ],
        ),
      ),
    );
  }

  Widget _buildStudentItem(String name, String project, double progress) {
    return Card(
      child: ListTile(
        leading: const CircleAvatar(backgroundImage: NetworkImage('https://i.pravatar.cc/150?img=3')), // Avatar giả
        title: Text(name),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(project),
            const SizedBox(height: 5),
            LinearProgressIndicator(value: progress, color: Colors.purple, backgroundColor: Colors.purple[100]),
          ],
        ),
        trailing: const Icon(Icons.message, color: Colors.purple),
      ),
    );
  }
}