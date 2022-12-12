#ifndef RANGE_HPP
#define RANGE_HPP

// Credit: https://stackoverflow.com/a/7185723

// Modified to allow specifying step size (including negative steps)

class iter_range
{
    public:
        class iterator
        {
            friend class iter_range;

            public:
                long int operator*() const
                {
                    return i_;
                }
                
                const iterator &operator++()
                {
                    i_ += step;
                    return *this;
                }
                
                iterator operator++(int)
                {
                    iterator copy(*this);
                    i_ += step;
                    return copy;
                }

                bool operator==(const iterator &other) const
                {
                    return i_ == other.i_;
                }
                
                bool operator!=(const iterator &other) const
                {
                    return i_ != other.i_;
                }

            protected:
                iterator(long int start, long int step = 1) : i_(start), step(step) {}

            private:
                unsigned long i_;
                long int step;
        };

        iterator begin() const { return begin_; }
        iterator end() const { return end_; }
        
        iter_range(long int begin, long int end, long int step = 1) : begin_(begin, step), end_(end) {}

    private:
        iterator begin_;
        iterator end_;

};

#endif