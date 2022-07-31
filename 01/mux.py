class mux:
    """
        if s0 == 0:
            out = a
        else:
            out = b
    """
    def __init__(self) -> None:
        self._output = []
        self._myMuxOutput = []

    def mux_method(self, a, b, s0) -> None:
        # multiplxer implementation with 15 gates using DNF 
        out = (a and not b and not s0) or \
            (not a and b and s0) or \
                (a and b and not s0) or \
                    (a and b and s0)
        self._output.append([a, b, s0, int(out)])
    
    def myFuncMux(self, a, b, s0) -> None:
        # multiplxer implementation with x gates using Karnaugh map
        out = (not s0 and a) or (s0 and b)
        self._myMuxOutput.append([a, b, s0, int(out)])
        
    def print_result(self, gates=None):
        lst = None
        if gates == 15:
            lst = self._output
        else:
            lst = self._myMuxOutput

        for _i, item in enumerate(lst):
            a = item[0]
            b = item[1]
            s0 = item[2]
            out = item[3]
            print(f"a: {a} | b: {b} | s0: {s0} -> out: {out}")

if __name__ == "__main__":
    myMux = mux()
    
    print("15 gates mux:\n__________")
    myMux.mux_method(0, 0, 0)
    myMux.mux_method(0, 1, 0)
    myMux.mux_method(0, 0, 1)
    myMux.mux_method(0, 1, 1)
    myMux.mux_method(1, 0, 0)
    myMux.mux_method(1, 1, 0)
    myMux.mux_method(1, 0, 1)
    myMux.mux_method(1, 1, 1)
    myMux.print_result(15)

    print("\n4 gates mux:\n________________")
    myMux.myFuncMux(0, 0, 0)
    myMux.myFuncMux(0, 1, 0)
    myMux.myFuncMux(0, 0, 1)
    myMux.myFuncMux(0, 1, 1)
    myMux.myFuncMux(1, 0, 0)
    myMux.myFuncMux(1, 1, 0)
    myMux.myFuncMux(1, 0, 1)
    myMux.myFuncMux(1, 1, 1)
    myMux.print_result()