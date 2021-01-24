
import arcpy
from arcpy import env
from arcpy.sa import *
import arcpy

arcpy.CheckOutExtension("spatial") #权限检查
arcpy.env.workspace="{待裁剪影像所在文件夹目录}" #，定义工作空间，需将待裁剪影像放在一个目录下
Inputfeature="{shp文件}" 
rasters=arcpy.ListRasters("*",{type})#将文件格式为tpye的数据放入rasters中，type:要裁剪的影像格式类型
for raster in rasters:#遍历rasters中的数据
     out={OutputFile}+"_clip_"+raster #这样输出的文件保留了全称和文件格式输出的时候文件名前面加了_clip_
     arcpy.gp.ExtractByMask_sa(raster,Inputfeature,out)#裁剪
