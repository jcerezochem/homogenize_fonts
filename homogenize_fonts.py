import xmgrace_parser as xmgr
import sys

# Default parameters
agrdefault_xsize   = 27.94 # 792
agrdefault_ysize   = 21.59 # 612
agrdefault_xyratio = 1.2941176470588236
texdefault_width   = 8 #cm
texdefault_font    = 12 #pt
# With these defaults (and ps2pdf_cst)
f = 74
# using (with standard ps2pdf)
## [scale=0.3]: fit_scale = 59*1.2
## [width=8cm]: fit_scale = 65*1.2

# Input
agr_file  = sys.argv[1]
tex_font  = float(sys.argv[2]) #12 # pt
tex_width = float(sys.argv[3]) #10 # cm
scale     = float(sys.argv[4]) #1 

print(f'AGR file    : {agr_file}')
print(f'Font in tex : {tex_font}')
print(f'Width in tex: {tex_width}')
print(f'Scaling     : {scale}')

# Edit AGR
agr = xmgr.AgrFile(agr_file)

# Get size for width=8 and fontsize=12pt (in the document)
# and using ps2pdf_cst.sh to generate pdf
# Factor with default parameters
fsize = agr.fontsize(tex_font) * f
# account for xsize
#fsize *= agr.get_size()[0]/agrdefault_xsize
# account for ysize
fsize *= agr.get_size()[1]/agrdefault_ysize
# account for width in tex file
fsize *= texdefault_width/tex_width
# account for changes in x/y ratio
fsize *= agr.get_size()[0]/agr.get_size()[1]/agrdefault_xyratio
# account for a factor related to tex font size
fsize *= 0.6275513886143352/agr.fontsize(tex_font) * (tex_font/texdefault_font)**2
# Apply scaling
fsize *= scale

# Apply fontsize and write
agr.set_fontsize(fsize)
agr.write(overwrite=True)
