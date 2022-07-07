import vtk
# 定义渲染窗口、交互模式
aRender = vtk.vtkRenderer()
Renwin = vtk.vtkRenderWindow()
Renwin.AddRenderer(aRender)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(Renwin)

# 定义个图片读取接口
#读取PNG图片就换成PNG_Reader = vtk.vtkPNGReader()
Jpg_Reader = vtk.vtkJPEGReader()
Jpg_Reader.SetNumberOfScalarComponents(1)
Jpg_Reader.SetFileDimensionality(3)  # 说明图像是三维的
 # 定义图像大小，本行表示图像大小为（512*512*240）
Jpg_Reader.SetDataExtent(0, 480, 0, 480, 0, 90) 
 # 设置图像的存放位置
Jpg_Reader.SetFilePrefix("C:/patient3_2/")
 # 设置图像前缀名字
 #表示图像前缀为数字（如：0.jpg）
Jpg_Reader.SetFilePattern("%s%d.jpg")
Jpg_Reader.Update()
Jpg_Reader.SetDataByteOrderToLittleEndian()

# 计算轮廓的方法
contour = vtk.vtkMarchingCubes()  
contour.SetInputConnection(Jpg_Reader.GetOutputPort())
contour.ComputeNormalsOn()
contour.SetValue(0, 255)


mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(contour.GetOutputPort())
mapper.ScalarVisibilityOff()

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.SetBackground([0.1, 0.1, 0.5])
renderer.AddActor(actor)

window = vtk.vtkRenderWindow()
window.SetSize(480, 480)
window.AddRenderer(renderer)


interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

# 开始显示
window.Render()
interactor.Initialize()
interactor.Start()
'''
作者：派大大大星
链接：https://juejin.cn/post/7027814515337084964
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''