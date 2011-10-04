This is a list of parameters present in different potential backends ("implementations") of the [[QGIS Processing Framework]] and a tentative common ground.

If possible, match datatype of QGIS parameters to implementations. (Hint on the list to look at WPS's dataypes)

## OTB parameters

* Input image
* Input complex image (for SAR imagery)
* Output image
* Input vector data
* Output vector data
* File name
* Directory name
* String
* Boolean
* Numeric (int/float as a first step)
* Choice (enumerated value)
* Geometry/CRS (specified by EPSG, WKT, image file, txt file containing a WKT..)
* DEM (SRTM directory, average elevation, arbitrary raster)
* Radius (=Int parameter, always with the name "Radius")
* Origin
* Spacing
* Size
* Region (= Origin + Size)
* Point/Index (for example, seed of region growing algorithm). in Qgis, possibility to select by mouse click on the canvas
RAM
* Interpolator Type
* Pixel Type (for output raster)
* Spatial subset/spectral subset, always available for input image parameters. Directly integrated in Input image parameter ?
* Parameter group
* Mathematical expression

## SAGA parameters

* PARAMETER_TYPE_Node 	
* PARAMETER_TYPE_Bool 	
* PARAMETER_TYPE_Int 	
* PARAMETER_TYPE_Double 	
* PARAMETER_TYPE_Degree 	
* PARAMETER_TYPE_Range 	
* PARAMETER_TYPE_Choice 	
* PARAMETER_TYPE_String 	
* PARAMETER_TYPE_Text 	
* PARAMETER_TYPE_FilePath 	
* PARAMETER_TYPE_Font 	
* PARAMETER_TYPE_Color 	
* PARAMETER_TYPE_Colors 	
* PARAMETER_TYPE_FixedTable 	
* PARAMETER_TYPE_Grid_System 	
* PARAMETER_TYPE_Table_Field 	
* PARAMETER_TYPE_PointCloud 	
* PARAMETER_TYPE_Grid 	
* PARAMETER_TYPE_Table 	
* PARAMETER_TYPE_Shapes 	
* PARAMETER_TYPE_TIN 	
* PARAMETER_TYPE_Grid_List 	
* PARAMETER_TYPE_Table_List 	
* PARAMETER_TYPE_Shapes_List 	
* PARAMETER_TYPE_TIN_List 	
* PARAMETER_TYPE_PointCloud_List 	
* PARAMETER_TYPE_DataObject_Output 	
* PARAMETER_TYPE_Parameters 	
* PARAMETER_TYPE_Undefined 	

"interactive parameters":

* point on canvas
* rect in canvas
* circle in canvas
* line in canvas

## Tentative common ground

* Raster = OTB Image = SAGA Grid = QgsRasterLayer (QComboBox)
* Vector = OTB vector data = SAGA Shape = QgsVectorLayer (QComboBox)
* URL = OTB File name = OTB Directory name = SAGA FilePath = FileName (QFileDialog)
* String = OTB String = SAGA String = SAGA Text = **default for everything not covered**, String (QLineEdit)
* Boolean = OTB Boolean = SAGA Bool = bool (QCheckbox)
* Number = OTB Numeric = OTB Radius = SAGA Int = SAGA Double = float (QSpinBox)
* Enumeration = OTB Choice = SAGA Choice = int (QComboBox)
* Tuple = OTB Origin = OTB Size = SAGA Range
* Rect = OTB Region = SAGA Rect
* Point = OTB Point/Index = SAGA Point
* List = OTB Parameter group = SAGA Grid List, Shapes_List, etc.

### Pseudoparameters
Control of module execution and feedback.

* State
* Message