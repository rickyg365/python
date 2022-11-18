import os 
import datetime

from openpyxl import Workbook

# Extra Features
from openpyxl import load_workbook
from openpyxl.drawing.image import Image


"""
Name: openpyxl Notes
Author: rickyg3
Date: 02/11/22


Table of Contents:
----------------------------------------------
* Create Workbook
* Worksheet manipulation

* Playing w/ Data Cells
	- Single Cell
	- Multi Cell
	- Values Only

* Manipulating Files
	- Saving File
	- Loading File

* Miscellaneous
	- Number Formats
	- Using Formulae
	- Merge/Unmerge Cells
	- Insert an Image
	- Fold (outline)

----------------------------------------------
"""


'''
.-----------------.
| Create Workbook |
'-----------------'

------------------------------------------------------------------------------------------
'''
workbook = Workbook()
'''
------------------------------------------------------------------------------------------
'''




# ------------------------------------------------------------------------------------------
# .------------------------.
# | Worksheet Manipulation |
# '------------------------'
# ------------------------------------------------------------------------------------------


'''
.------------------------.
| Worksheet Manipulation |
'------------------------'

A workbook is always created with at least one worksheet,
'''
ws = workbook.active

'''
This is set to 0 by default. 
Unless you modify its value using create_sheet(), 
you will always get the first worksheet by using this method.
'''
ws1 = workbook.create_sheet("Mysheet") # insert at the end (default)
ws2 = workbook.create_sheet("Mysheet", 0) # insert at first position
ws3 = workbook.create_sheet("Mysheet", -1) # insert at the penultimate position

'''
Sheets are given a name automatically when they are created. 
They are numbered in sequence (Sheet, Sheet1, Sheet2, …). 
You can change this name at any time with:
Worksheet.title 
'''
ws.title = "New Title"

'''
You can review the names of all worksheets of the workbook with: 
Workbook.sheetnames 
'''
print(workbook.sheetnames)  # OUTPUT >>> ['Sheet2', 'New Title', 'Sheet1']

'''
You can loop through worksheets
'''
for sheet in workbook:
	print(sheet.title)


'''
You can create copies of worksheets within a single workbook
'''
source = workbook.active
target = workbook.copy_worksheet(source)


'''
Final Note:
------------------------------------------------------------------------------------------
Only cells (including values, styles, hyperlinks and comments) 
and certain worksheet attribues (including dimensions, format and properties) are copied. 
All other workbook / worksheet attributes are not copied - e.g. Images, Charts.

You also cannot copy worksheets between workbooks. 
You cannot copy a worksheet if the workbook is open in read-only or write-only mode.
------------------------------------------------------------------------------------------
'''




# ------------------------------------------------------------------------------------------
# .-----------------------.
# | Playing w/ Data Cells |
# '-----------------------'
# ------------------------------------------------------------------------------------------


'''
.-------------.
| Single Cell |
'-------------'

------------------------------------------------------------------------------------------

Cells acn be accessed directly as a key, or
you can also use the worksheet.cell() function 
'''
# Key Method, key='a1'
ws['a1'] = 24

# Cell Method
ws.cell(row=4, column=2, value=10)

'''
Side Note:

When a worksheet is created in memory, it contains no cells. 
They are created when first accessed.

[ Warning ]

Because of this feature, scrolling through cells 
instead of accessing them directly will create them all in memory, 
even if you dont assign them a value.

Something like
------------------------------------------------------------------------------------------

for x in range(1,101):
	for y in range(1,101):
		ws.cell(row=x, column=y)

------------------------------------------------------------------------------------------

will create 100x100 cells in memory, for nothing.

------------------------------------------------------------------------------------------
'''

# Break

"""
.------------.
| Multi Cell |
'------------'

------------------------------------------------------------------------------------------

Ranges of cells can be accessed using slicing
"""
cell_range = ws['A1':'C2']

'''
Ranges of rows or columns can be obtained similarly:
'''
col_c = ws['C']
col_range = ws['C:D']
row10 = ws[10]
row_range = ws[5:10]

'''
You can also use the Worksheet.iter_rows() method:
'''
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
	for cell in row:
		print(cell)

# Output:
# <Cell Sheet1.A1>
# <Cell Sheet1.B1>
# <Cell Sheet1.C1>
# <Cell Sheet1.A2>
# <Cell Sheet1.B2>
# <Cell Sheet1.C2>
 
'''
Likewise the Worksheet.iter_cols() method will return columns:
'''
for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
	for cell in col:
		print(cell)

# Output:
# <Cell Sheet1.A1>
# <Cell Sheet1.A2>
# <Cell Sheet1.B1>
# <Cell Sheet1.B2>
# <Cell Sheet1.C1>
# <Cell Sheet1.C2>

'''
Note: 

For performance reasons the Worksheet.iter_cols() method 
is not available in read-only mode.
'''

'''
If you need to iterate through all the rows or columns of a file, you can instead use the Worksheet.rows property:

>>> ws = wb.active
>>> tuple(ws.rows)

or the Worksheet.columns property:

>>> tuple(ws.columns)

------------------------------------------------------------------------------------------
'''


# Break

'''
.-------------.
| Values Only |
'-------------'

------------------------------------------------------------------------------------------

If you just want the values from a worksheet 
you can use the Worksheet.values property. 

This iterates over all the rows in a worksheet 
but returns just the cell values:

'''

for row in ws.values:
	for value in row:
		print(value)


# Cann add rows of data
ws.append([1, 2, 3])

# Auto converts python types
ws['b1'] = datetime.datetime.now()
'''
------------------------------------------------------------------------------------------
'''




# ------------------------------------------------------------------------------------------
# .--------------------.
# | Manipulating Files |
# '--------------------'
# ------------------------------------------------------------------------------------------


'''
.-------------.
| Saving File |
'-------------'

------------------------------------------------------------------------------------------

The simplest and safest way to save a workbook is by using:

Workbook.save()

'''
workbook.save("second_test.xlsx")

'''
Warning:

This operation will overwrite existing files without warning.

Note:
The filename extension is not forced to be xlsx or xlsm, 
although you might have some trouble 
opening it directly with another application if you dont use an official extension.

As OOXML files are basically ZIP files, 
you can also open it with your favourite ZIP archive manager.

------------------------------------------------------------------------------------------
'''



'''
.-------------.
| Loading File |
'-------------'

------------------------------------------------------------------------------------------

Note:

*Dont forget import*
from openpyxl import load_workbook

'''

wb2 = load_workbook('test.xlsx')
'''
------------------------------------------------------------------------------------------
'''




# ------------------------------------------------------------------------------------------
# .---------------.
# | Miscellaneous |
# '---------------'
# ------------------------------------------------------------------------------------------


'''
.----------------.
| Number Formats |
'----------------'

------------------------------------------------------------------------------------------

'''
# set date using a Python datetime
ws['A1'] = datetime.datetime(2010, 7, 21)
ws['A1'].number_format  # OUTPUT >>> 'yyyy-mm-dd h:mm:ss'
'''
------------------------------------------------------------------------------------------
'''



'''
.----------------.
| Using Formulae |
'----------------'

------------------------------------------------------------------------------------------

'''
# add a simple formula
ws["A1"] = "=SUM(1, 1)"
'''
------------------------------------------------------------------------------------------
'''



'''
.---------------------.
| Merge/Unmerge Cells |
'---------------------'

------------------------------------------------------------------------------------------

When you merge cells all cells but the top-left one are removed from the worksheet. 
To carry the border-information of the merged cell, 
the boundary cells of the merged cell are created as MergeCells which always have the value None. 

See Styling Merged Cells for information on formatting merged cells.

'''
# This
ws.merge_cells('A2:D2')
ws.unmerge_cells('A2:D2')

# or equivalently
ws.merge_cells(start_row=2, start_column=1, end_row=4, end_column=4)
ws.unmerge_cells(start_row=2, start_column=1, end_row=4, end_column=4)
'''
------------------------------------------------------------------------------------------
'''



'''
.--------------------.
| Inserting an Image |
'--------------------'

------------------------------------------------------------------------------------------

*needs import*
from openpyxl.drawing.image import Image

'''
# create an image
img = Image('logo.png')

# add to worksheet and anchor next to cells
ws.add_image(img, 'A1')
workbook.save('logo.xlsx')
'''
------------------------------------------------------------------------------------------
'''



'''
.---------------.
| Fold(outline) |
'---------------'

------------------------------------------------------------------------------------------
'''
# Folding??
ws.column_dimensions.group('A','D', hidden=True)
ws.row_dimensions.group(1,10, hidden=True)
'''
------------------------------------------------------------------------------------------
'''


# .-------------.
# | End of File |
# '-------------'
