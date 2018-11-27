// Terminating iterations over ranges with iterator sentinals
// we will build an iterator together with a range class,
// which enables us to iterate over a string with unknown lengh, without
// finding the end position in advance
#include <iostream>

// The iterator sentinel is a very central element of this section.
// Its class definition can stay completely empty.
class cstring_iterator_sentinel {};

// Implement the iterator.  It will contain a string pointer, which
// is the container we iterate ove
class cstring_iterator {
    const char *s {nullptr};

public:
	// the constructor initializes the internal string pointer to whatever
	// string the user provides. Let's make the constructor explicit in
	// order to prevent accidental implicit conversion
    explicit cstring_iterator(const char *str)
        : s{str}
    {}

	// when derefercing the iterator at some point, it will just return
	// the character value at this position
	char operator*() const { return *s; }

    // incrementing the iterator just increments the position in the string
	cstring_iterator& operator++() {
        ++s;
        return *this;
    }

	// compare iterators with sentinals
    bool operator!=(const cstring_iterator_sentinel) const {
        return s != nullptr && *s != '\0';
    }
};

// so that a range-base for loop can be used
class cstring_range {
    const char *s {nullptr};

public:
    cstring_range(const char *str)
        : s{str}
    {}

    // return a normal cstring_iterator from the begin function
	cstring_iterator          begin() const { return cstring_iterator{s}; }
	
	// returns a sentinel type
    cstring_iterator_sentinel end()   const { return {}; }
};

int main(int argc, char *argv[])
{
    if (argc != 2) {
        std::cout << "Please provide one parameter.\n";
        return 1;
    }

    const char * const param {argv[1]};

    for (char c : cstring_range(param)) {
        std::cout << c;
    }
	std::cout << '\n';
	
	return 0;
}
