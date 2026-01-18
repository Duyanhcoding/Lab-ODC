import 'package:flutter/material.dart';
import 'screen/auth/login_screen.dart';

void main() {
  runApp(const LabOdcApp());
}

class LabOdcApp extends StatelessWidget {
  const LabOdcApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'LabOdc',
      debugShowCheckedModeBanner: false, // Tắt chữ Debug ở góc phải
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const LoginScreen(), // Chạy màn hình Login đầu tiên
    );
  }
}