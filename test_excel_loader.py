import pandas as pd
import os

print("🎓 University Timetable Loader Test")
print("=" * 40)

# Path to your university Excel file
excel_file = "sample_data/university_timetable.xlsx"

# Check if the file exists first
if os.path.exists(excel_file):
    print(f"✅ Found Excel file: {excel_file}")
    
    try:
        # Load ALL sheets at once (Monday through Saturday)
        all_sheets = pd.read_excel(excel_file, sheet_name=None)
        
        print(f"📊 Total sheets found: {len(all_sheets)}")
        print(f"📋 Sheet names: {list(all_sheets.keys())}")
        
        # Let's look at Monday sheet as an example
        monday_sheet = all_sheets['Monday']
        print(f"\n🔍 Monday sheet analysis:")
        print(f"   Dimensions: {monday_sheet.shape[0]} rows x {monday_sheet.shape[1]} columns")
        
        # Show the first few time slots (first row)
        print(f"\n⏰ Time slots found:")
        time_row = monday_sheet.iloc[0, 1:6]  # Skip first column, show 5 time slots
        for i, time_slot in enumerate(time_row):
            if pd.notna(time_slot):
                print(f"   Column {i+1}: {time_slot}")
        
        # Show the first few rooms (first column) 
        print(f"\n🏠 Room numbers found:")
        room_column = monday_sheet.iloc[1:6, 0]  # Skip first row, show 5 rooms
        for i, room in enumerate(room_column):
            if pd.notna(room):
                print(f"   Row {i+1}: {room}")
        
        # Show a sample subject cell
        print(f"\n📚 Sample subject cell:")
        sample_cell = monday_sheet.iloc[1, 1]  # Row 1, Column 1
        print(f"   Content: '{sample_cell}'")
        
        print(f"\n✅ Excel file loaded successfully! Ready for data processing.")
        
    except Exception as e:
        print(f"❌ Error loading Excel file: {e}")
        print("💡 Make sure your Excel file isn't open in another program")
        
else:
    print(f"❌ Excel file not found: {excel_file}")
    print("💡 Copy your university Excel file to the sample_data/ folder")
    print("💡 Rename it to 'university_timetable.xlsx'")
