-module(length).
-export([length/1]).

length(L) ->
    length(L, 0).

length([], Acc) -> Acc;
length([_|Rest], Acc) ->
    length(Rest, Acc+1).
