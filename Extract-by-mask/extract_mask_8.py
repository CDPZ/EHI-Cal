
import arcpy
from arcpy import env
from arcpy.sa import *
import arcpy

arcpy.CheckOutExtension("spatial") #Ȩ�޼��
arcpy.env.workspace="{���ü�Ӱ�������ļ���Ŀ¼}" #�����幤���ռ䣬�轫���ü�Ӱ�����һ��Ŀ¼��
Inputfeature="{shp�ļ�}" 
rasters=arcpy.ListRasters("*",{type})#���ļ���ʽΪtpye�����ݷ���rasters�У�type:Ҫ�ü���Ӱ���ʽ����
for raster in rasters:#����rasters�е�����
     out={OutputFile}+"_clip_"+raster #����������ļ�������ȫ�ƺ��ļ���ʽ�����ʱ���ļ���ǰ�����_clip_
     arcpy.gp.ExtractByMask_sa(raster,Inputfeature,out)#�ü�
