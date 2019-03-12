const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0b0e10", /* black   */
  [1] = "#34D7E8", /* red     */
  [2] = "#2B99A9", /* green   */
  [3] = "#46C7D6", /* yellow  */
  [4] = "#278B96", /* blue    */
  [5] = "#3AB5C3", /* magenta */
  [6] = "#2CF1FD", /* cyan    */
  [7] = "#99e0e9", /* white   */

  /* 8 bright colors */
  [8]  = "#95a7b6",  /* black   */
  [9]  = "#31ffff",  /* red     */
  [10] = "#2ad1e9", /* green   */
  [11] = "#48ffff", /* yellow  */
  [12] = "#26becf", /* blue    */
  [13] = "#3af8ff", /* magenta */
  [14] = "#25ffff", /* cyan    */
  [15] = "#c8ffff", /* white   */

  /* special colors */
  [256] = "#0b0e10", /* background */
  [257] = "#c8ffff", /* foreground */
  [258] = "#c8ffff",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
