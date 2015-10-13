-module(merge).
-export([merge/2]).

merge(A, B) ->
    merge(A, B, []).

merge([], [], Acc) -> Acc;
merge([], B, Acc) -> Acc ++ B;
merge(A, [], Acc) -> Acc ++ A;
merge([X|Xs], B=[Y|_], Acc) when X < Y ->
    merge(Xs, B, Acc ++ [X]);
merge(A, [Y|Ys], Acc) ->
    merge(A, Ys, Acc ++ [Y]).

