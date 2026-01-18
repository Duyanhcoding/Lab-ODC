class Project {
  final String id;
  final String name;
  final String status;
  final String description;

  Project({
    required this.id,
    required this.name,
    required this.status,
    required this.description,
  });

  // Hàm chuyển đổi từ JSON của Server sang Object Dart
  factory Project.fromJson(Map<String, dynamic> json) {
    return Project(
      // Kiểm tra xem server trả về '_id' hay 'id'
      id: json['_id'] ?? json['id']?.toString() ?? '',
      // Kiểm tra xem server trả về 'name' hay 'title'
      name: json['name'] ?? json['title'] ?? 'Dự án không tên',
      status: json['status'] ?? 'Active',
      description: json['description'] ?? 'Chưa có mô tả',
    );
  }
}