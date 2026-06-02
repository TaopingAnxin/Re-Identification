import scipy.io as scio
import numpy as np

def summarize_array(array, max_elements=10):
    """总结数组内容，如果数组太大则截断"""
    if array.size > max_elements:
        flat_array = array.flatten()
        summary = np.array2string(flat_array[:max_elements], separator=', ')
        return f"{summary}, ... (total {array.size} elements)"
    else:
        return np.array2string(array, separator=', ')

def inspect_mat_file(file_path, max_elements=10):
    """检查并打印 .mat 文件的内容，包括部分数据"""
    try:
        data = scio.loadmat(file_path)
        print(f"\nFile: {file_path}")
        print("Contents:")
        for key, value in data.items():
            if key.startswith('__'):
                continue  # 跳过特殊键
            if isinstance(value, np.ndarray):
                print(f"  {key}: type={type(value)}, shape={value.shape}")
                print(f"    data: {summarize_array(value, max_elements)}")
            else:
                print(f"  {key}: {value}")
    except Exception as e:
        print(f"Error loading {file_path}: {e}")

# 你的 .mat 文件路径
mat_file_path = '/home/pingpai/mnt_10T/ste-net/ste-net-master/data/PRID/prid_2011_event/cam_a/person_0002/001.mat'

# 检查 .mat 文件内容
inspect_mat_file(mat_file_path)