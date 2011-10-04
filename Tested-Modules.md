Please list any modules you have tested and work. If you see a module listed that didn't work for you, comment & indicate the circumstances.

The wiki page [[Module Support]] lists modules that, in principle, should work, but have not been necessarily tested.

## List of tested modules
### Working
* other > Pythagora's Tree
* lectures > 01: My first module
* introducing module programming > 02: Pixel by pixel operations with two grids
* introducing module programming > 03: Direct neighbours
* introducing module programming > 05: Direct neighbours - slope and aspect
* introducing module programming > 07: Extended neighbourhoods - catchment areas (trace flow)
* introducing module programming > 08: Extended neighbourhoods - catchment areas (parallel)
* introducing module programming > 09: Extended neighbourhoods - catchment areas (recursive)
* introducing module programming > 11: Dynamic Simulation - Soil Nitrogen Dynamics
* introducing module programming > 14: Vectorising channel lines [lines are broken, but this should have nothing to do with the plugin]
* introducing module programming > Cell Balance
* shapes > Contour Lines from Grid
* terrain analysis > Analytical Hillshading
* terrain analysis > D8 Flow Analysis
* terrain analysis > Diurnal Anisotropic Heating
* terrain analysis > Flat Detection
* terrain analysis > Slope, Aspect, Curvature
* terrain analysis > Surface Specific Points
* filter > DTM Filter (slope-based)
* geostatistics > Radius of Variance (Grid)

### Not working or problematic
* introducing module programming > 10: Dynamic Simulation - Life [no input grid specified]
* introducing module programming > 12: First steps with shapes [seems to show always the same displacement, regardless of parameters; also, max value of parameters is 4 digits, probably too low]
* shapes > Add Coordinates to points [nothing done]
* tools > Aggregate [no output]
* terrain analysis > Burn Stream Network into DEM [no visible effect of changing parameters]
* terrain analysis > Sink Drainage Route Detection [no visible effect of changing parameters]
* terrain analysis > Upslope Area [module execution failed]
* tools > Change Cell Values [no visible results]
* shapes > Convex Hull (one hull for all shapes) crashes QGIS with segfault:
GEOS error: IllegalArgumentException: point array must contain 0 or >1 elements
* analysis > Spatial Point Pattern Analysis [same as Covex Hull]

### Need proper sample data to be tested
* analysis > Accumulated Cost (Anisotropic)