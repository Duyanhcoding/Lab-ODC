class User {
  final String id;
  final String name;
  final String email;
  final String role; // Quan trọng: enterprise, talent, mentor, admin

  User({required this.id, required this.name, required this.email, required this.role});

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['_id'] ?? json['id'] ?? '',
      name: json['name'] ?? 'User',
      email: json['email'] ?? '',
      // Nếu server trả về số (1,2,3) thì map sang chuỗi, nếu trả chuỗi thì giữ nguyên
      role: json['role'] ?? 'talent', 
    );
  }
}