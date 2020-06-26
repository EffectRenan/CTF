**Challenge:** ropes

Execute: `echo -n $(strings ropes | grep '{' | cut -d ' ' -f4) && strings ropes | grep '}' | cut -d ' ' -f4'`

**Flag:** flag{r0pes_ar3_just_l0ng_str1ngs}
