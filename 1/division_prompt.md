The text already has markers for 
```
### PAGE
### CITATION
```
Use the line numbers in [] to write a json file 

Together they should add the following markers:

Section Marker Tags:
```
# RIM_KHANG     	 // Major divisions (རིམ་ཁང་)
## SA_BCAD      	 // Topical subdivisions (གཏན་ལ་དབབ་པ་)
### DIMENSION     	 // Analytical dimensions (མཚན་ཉིད་/རྟེན་/ཡུལ་)
#### PRACTICE        // Practice instruction blocks (སྒོམ་ཚུལ་)
```

include a title case section title eg.

#### PRACTICE: Twelve Links of Dependent Origination as Delusion

Note, sometimes you may have to stack multiple section headers between two lines because we begin a new major section.   eg at a new RIM_KHANG for example you might have a full stack of 

```
# RIM_KHANG     
## SA_BCAD      	
### DIMENSION     
```
Next... Meter Market Tags:
```
#### VERSE 		     // Begins a metered verse block 
#### /VERSE	 		 // Ends a metered verse block 
```
every verse section must explicitly specify the metrical form in parenthesis () eg.
```
#### VERSE: bdun tshig  7-7-7-7; 4:3 Stress
[...]
#### /VERSE
```
Do not Title the VERSE and 
Do not add any comment to the /VERSE ending

Finally... CITATAION /CITATION tags:

The file already contains many CITATION tags for where Longhenpa cite's his root text amid autocommentary.
If there are additional CITATION tags required to indicate beginning of root text section add them to your json.
The ending of each /CITATION is not yet marked.  
Add /CITATION points to your json to indicate where the text returns to autocommentary from root text.

json file should be in format of list of lists eg.
```
[
[21,"#### PRACTICE: Twelve Links of Dependent Origination as Delusion"],
[33, "#### VERSE: bdun tshig (བདུན་ཚིག་) 7-7-7-7; 4:3 Stress"],
[47,"####/VERSE"]
]
```
Be precise; Tibetan khenpo level document mastery!

Next block of pages of text attached, produce valid json for the app: 

