static const char norm_fg[] = "#c8ffff";
static const char norm_bg[] = "#0b0e10";
static const char norm_border[] = "#95a7b6";

static const char sel_fg[] = "#c8ffff";
static const char sel_bg[] = "#2B99A9";
static const char sel_border[] = "#c8ffff";

static const char urg_fg[] = "#c8ffff";
static const char urg_bg[] = "#34D7E8";
static const char urg_border[] = "#34D7E8";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
