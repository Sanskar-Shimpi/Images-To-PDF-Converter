from PIL import Image
import os
import time

n_Dir = input('Enter Folder Name Where Images Are Stored: ')
l_images = os.listdir(f'/storage/emulated/10/{n_Dir}')

images = [
    Image.open(f"/storage/emulated/10/{n_Dir}/" + f)
    for f in l_images
]

print('\nProcessing...')

time.sleep(2)

file_name = input('\nEnter Name Of PDF To Be Saved As: ')
print('\nConverting... Please Wait!')
images[0].save(f"{file_name}.pdf" ,resolution=100.0, save_all=True, append_images=images[1:])



for items in l_images:	
	png = Image.open(f'/storage/emulated/10/{n_Dir}/{items}')
png.load()
background = Image.new("RGB", png.size, (255, 255, 255))
background.paste(png, mask=png.split()[1])

print('\nSuccess!\nThank You For Using Our System!')