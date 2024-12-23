import xarray as xr
import os

# 指定输入文件夹路径
input_directory = "C:/Users/17865/Desktop/MIX/MIX2010/CB05/"  # 替换为你的输入文件夹路径
# 指定输出路径
base_output_path = "C:/Users/17865/Desktop/MIX/MIX2010/CB05/Output/"  # 请替换为你的输出路径
os.makedirs(base_output_path, exist_ok=True)  # 创建基础输出路径（如果不存在）

# 遍历输入目录中的所有文件
for filename in os.listdir(input_directory):
    if filename.endswith('.nc'):  # 只处理.nc文件
        input_file = os.path.join(input_directory, filename)

        # 打开数据集
        ds = xr.open_dataset(input_file)

        # 获取时间、经度和纬度的维度
        time = ds['time']
        variables = list(ds.data_vars)  # 获取所有变量名

        # 遍历时间和变量，拆分数据并保存
        for t in range(len(time)):
            # 获取当前时间
            month = int(time[t].values)  # 假设时间是从1开始的整数
            year = 2010  # 根据您的需求设置年份

            # 创建每个月的文件夹
            month_folder = os.path.join(base_output_path, f"2010{month}")  # e.g., "month_1"
            os.makedirs(month_folder, exist_ok=True)  # 创建月份文件夹（如果不存在）

            for var in variables:
                # 提取当前变量和时间点的数据
                data = ds[var].isel(time=t)

                # 创建新的数据集
                new_ds = xr.Dataset({var: data})

                # 构造新的文件名（将大写字母转换为小写字母）
                pollutant_name = var.split('_')[1]  # 假设污染物名称在变量名的第一部分
                section_name = var.split('_')[2].lower()  # 假设污染物名称在变量名的第二部分
                m_name = var.split('_')[0]  # 假设污染物名称在变量名的第二部分
                new_file_name = f"{year}_{month}_{section_name}_{m_name}_{pollutant_name}.nc"  # e.g., 2010_1_residential_bc.nc
                full_output_path = os.path.join(month_folder, new_file_name)  # 生成完整的输出路径

                # 保存为新的 NetCDF 文件
                new_ds.to_netcdf(full_output_path)

        ds.close()  # 关闭数据集以释放资源

print("所有数据拆分完成！")
