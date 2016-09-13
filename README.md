Dumb simple implementation of two Turing machines, straight from his paper
[On Computable Numbers, With An Application To The Entscheidungsproblem](http://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf).

A better implementation would consist of an interpreter for his operation
syntax, along with stepping through the operations one op at a time, pretty
printing the tape each time so that we can witness it working, rather than just
computing the final result. A graphical animation / interface would clearly be
ideal, as absent that, reasoning about state machines of this form goes from
incredibly difficult to worse than incredibly difficult.
