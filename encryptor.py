import os


class FileEncryptor:
    def __init__(self, password):
        self.key = self._generate_key(password)

    def _generate_key(self, password):
        # 使用密码生成密钥 (简单示例)
        key = hash(password) % 256
        return key

    def _encrypt_byte(self, byte):
        # 对单个字节进行加密（异或和位移操作）
        encrypted_byte = byte ^ self.key
        encrypted_byte = ((encrypted_byte << 3) & 0xFF) | ((encrypted_byte >> 5) & 0xFF)
        return encrypted_byte

    def _decrypt_byte(self, byte):
        # 对单个字节进行解密（逆向位移和异或操作）
        decrypted_byte = ((byte >> 3) & 0xFF) | ((byte << 5) & 0xFF)
        decrypted_byte = decrypted_byte ^ self.key
        return decrypted_byte

    def encrypt_file(self, input_file_path, output_file_path):
        with open(input_file_path, 'rb') as input_file, open(output_file_path+, 'wb') as output_file:
            while (byte := input_file.read(1)):
                encrypted_byte = self._encrypt_byte(ord(byte))
                output_file.write(bytes([encrypted_byte]))
        print(f"File encrypted and saved to: {output_file_path}")

    def decrypt_file(self, input_file_path, output_file_path):
        with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
            while (byte := input_file.read(1)):
                decrypted_byte = self._decrypt_byte(ord(byte))
                output_file.write(bytes([decrypted_byte]))
        print(f"File decrypted and saved to: {output_file_path}")
