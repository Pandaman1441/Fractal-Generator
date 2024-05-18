# Code Smells Report - 5.0

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
    *   You do not need to list code smells in any particular order
*	Describe the smell and why it is a problem
*	Copy the offensive code between `` ``` ``
*	Describe how you can fix it
    *   We will follow up on these notes to make sure it was really fixed!


### These are some of the code smells you may find in the starter code:

0.  **Magic** numbers
    *   Numeric literals in critical places without any context or meaning
    *   "Does `256` over here have anything to do with the `256` over there?"
1.  **Global** variables
    *   Used to avoid passing a parameter into a function
    *   Used to return an extra value from a function
    *   There are better ways to meet both of these needs!
2.  **Poorly-named** variables
    *   Short variable names are okay in some contexts:
        *   `i` or `j` as a counter in a brief `for` loop
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
        *   Otherwise, short names should be avoided
    *   Variables with really, really long names make code harder to read
    *   Variables that override or "shadow" other identifiers
        *   Builtin Python functions such as `input`, `len`, `list`, `max`, `min` and `sum` are especially susceptible to this
    *   Variable names should strike a good balance between brevity and descriptiveness
3.  Comments that share **too much information**
    *   When almost every line of code is has an explanatory comment, it is likely true that variable and function names were poorly chosen
    *   Write code that speaks for itself
4.  Comments that **lie**
    *   An out-of-date remark that longer accurately describes the code
    *   Bad advice left by a developer without a clue
5.  Too many arguments
    *   Seen when more than a handful of parameters are passed to a function/method
    *   Parameters that are passed in but left unused
    *   Instead, accumulate parameters into a collection such as a dict
6.  Function/Method that is too long
    *   Too many lines of code typically happens because the function/method has too many different responsibilities
    *   Generally, a method longer than a dozen lines should make you ask yourself "can I split this into smaller, more focused pieces?"
7.  Complex decision trees
    *   Too long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Are all of the branches possible to reach?
    *   Has every branch been tested?
8.  Spaghetti code
    *   Heaps of meandering code without a clear goal
    *   Functions/objects used in inconsistent ways
    *   Many variables are used to keep track of 
    *   Conditional statements with long, confusing Boolean expressions
    *   Boolean expressions expressing double negatives; ex. `if not undone: ...`
    *   Code that makes you say "It would be easier to rewrite this than to understand it"
9.  Redundant code
    *   A repeated statement which doesn't have an effect the second time
    *   ```
        i = 7
        print(i)
        i = 7
        ```
    *   Ask yourself whether it makes any difference to be run more than once.
10. Dead code
    *   A piece of code that is not used (usually because it is obsolete)
    *   Blocks of commented-out code that serve no purpose and clutter up the file

If you see something that is not covered on this list, please add it to this report.


### Template

0.  Smell at `file` [lines xx-yy or general location]
    *   [Brief description of smell]
    *   [Code Snippet between triple-backquotes `` ``` ``]
    *   [How to resolve]


### Example

0.  Redundant Code at `src/main.py` [lines 32, 34]
    *   The import statement `import mbrot_fractal` occurs twice.  A second occurrence doesn't do it better than the first.
    *   ```python
        import mbrot_fractal  	    	       
        import phoenix_fractal as phoenix  	    	       
        import mbrot_fractal  	    	       
        ```
    *   This is easily resolved by deleting the second `import` statement.
    

## Code Smells

##Magic numbers smells
*   Magic numbers in mbrot_fractal.py [lines 50, 114 - 117]
    *   random variables that have arbitrary values
    ```
    MAX_ITERATIONS = -1
    .
    .
    .
    MAX_ITERATIONS = 115
    z = 0
    seven = 7.0
    TWO = 2
    ```
    *   I think all these can be deleted and use the literal numbers for some

##Global variables smells
*   global variables in mbrot_fractal.py [lines 159,160]
    *   sets these variables as global only to use it in the same function
    ```
    global MAX_ITERATIONS
    global iter
    ```
    *   can just delete these lines as the don't do anything outside of the function

##Poorly-named variables
*   poorly-named variable in main.py [line 81]
    *   The variable name is too long
    ```
    sysargv1_not_mndlbrt_frctl = MBROTS.count(sys.argv[1])
    ```
    *   Rename sysargv1_not_mndlbrt_frctl to something simpler like inMBROT

##Comments that share too much information
*   comments that share too much information [line 168 - 174]
    *   this comment doesn't need to be in the code and could be in a plan instead
    ```
    # XXX: the program used to crash with the error
    #   TypeError: 'int' object is not callable
    #
    # maybe it had something to do with 'len' being an integer variable
    # instead of a function variable.
    # Somebody from StackOverflow suggested I do it this way
    # IDK why, but it stopped crashing, and taht's all that matters!
    ```
    *   This whole comment can be deleted

##Comments that lie
*   comment that lies in main.py [line 121]
    *   I think this comment is outdated or just in the wrong spot
    ```
    # Otherwise, quit with an error message to help the user learn how to run it
    pass
    fratcal = sys.argv[1]
    ```
    *   Just deleting this comment will suffice

##Too many arguments
*   too many arguments in phoenix_fractal.py [lines 251 - 261]
    *   calls for the cols variable but doesn't use it in the function
    ```
    def pixelsWrittenSoFar(rows, cols):
    portion = (512 - rows) / 512
    pixels = (512 - rows) * 512
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    # print(f"{pixels} pixels have been output so far")
    # return pixels
    # return '[' + status_percent + ' ' + status_bar + ']'
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))
    ```
    *   if the function works without using cols then we can just remove it

##Function/Method that is too long
*   function that is too long in phoenix_fractal.py [lines 146 - 171]
    *   Randomly has the code to setup the gui in the painting function
    ```
        tk_Interface_PhotoImage_canvas_pixel_object.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?

    # Create the TK PhotoImage object that backs the Canvas Objcet
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((s/2, s/2), image=p, state="normal")
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # But it is how Larry wrote it the tutorial
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Larry's a smart guy.  I'm sure he has his reasons.

    # Total number of pixels in the image, AKA the area of the image, in pixels
    area_in_pixels = 640 * 640

    # pack the canvas object into its parent widget
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Does this even matter?
    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
    size = abs(max[0] - min[0]) / s

    # pack the canvas object into its parent widget
    tk_Interface_PhotoImage_canvas_pixel_object.pack()
    ```
    *   Create a new function to place this code in

##Complex decision trees
*   complex decision trees
    *   Has several indentations that it doesn't need
    ```
    for key in dictionary:
        if key in dictionary:
            if key == name:
                value = dictionary[key]
                return key
    ```
    *   we can just iterate through the dictionary until we find the name and return that key

##Spaghetti code
*   Spaghetti code in main.py [lines 85 - 117]
    *   prints out a list of fractals but prints out the phoenix and mandlebrot fractals in different ways for no reason and has several variables throughout the code
    ```
    if not arg_is_phoneix and sysargv1_not_mndlbrt_frctl == 0:
    print("ERROR:", sys.argv[1], "is not a valid fractal")    #
    print("Please choose one of the following:")             ###
    quit = False                                           #######
    next = ''                                              #######
    iter = 0                                                #####
    while not quit:                             #     ## ########### ###
        next = PHOENX[iter]                      ### #################### ## #
        print("\t%s" % next)                      ###########################
                                              # ############################
        if PHOENX[iter] == 'shrimp-cocktail': ################################
            break                            ####################################
                            #    ## #       ###################################
        else:               ##########     ######################################
            iter += 1     ##############   ####################################
                     ########################################################
              ######################################## CODE IS ART #########
                     ########################################################
    exit = None          ############################## (c) 2022 #############
    i = 0                 ##############   #####################################
    i = 0                   ##########     ####################################
    fractal = ''            #    ## #       ####################################
                                             #################################
    while not exit:                          ################################
        print("\t" + MBROTS[i])               #  ############################
        if PHOENX[iter] =='shrimp-cocktail':    ######################### ####
            if MBROTS[i]  == 'starfish':       ### #  ## ##############   #
                                              #             #####
                i = i + 1                                  #######
                exit = PHOENX[iter] =='shrimp-cocktail'    #######
                i -= 1 #need to back off, else index error   ###
                exit = exit and MBROTS[i]  == 'starfish'      #
        i = i + 1
    ```
    *   I think you can just add the two lists together then iterate through the new list to print out options

##Redundant code
*   redundant code in main.py [lines 104,105]
    *   i is set to 0 twice
    ```
    i = 0                 ##############   #####################################
    i = 0                   ##########     ####################################
    ```
    *   I can delete one of these lines

*   redundant code in mbrot_fractal.py [lines 33,41]
    *   first line imports several functions from math, the second line imports all of math
    ```
    from math import sqrt, cos, cosh, sin, sinh, remainder, acos, acosh, asin, asinh
    .
    .
    .
    import math
    ```
    *   Probably just delete the first line incase there is function used that isn't in that list

##Dead code
*   dead code in main.py [lines 70,71]
    *   This block doesn't get used
    ```
    if len(sys.argv) < 1:
    print ("Usage: The first argument needs to name a fractal")
    ```
    *   I think I can just delete this code and nothing would change

