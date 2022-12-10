#ifndef LINES_HPP
#define LINES_HPP

// Credit: https://stackoverflow.com/a/70400447

#include <string>
#include <iterator>
#include <istream>

struct line_iterator {
  using iterator_category = std::input_iterator_tag;
  using value_type = std::string;
  using difference_type = std::ptrdiff_t;
  using reference = const value_type&;
  using pointer = const value_type*;

  line_iterator(): input_(nullptr) {}
  line_iterator(std::istream& input): input_(&input) { ++*this; }

  reference operator*() const { return s_; }
  pointer operator->() const { return &**this; }

  line_iterator& operator++() {
    if (!std::getline(*input_, s_)) input_ = nullptr;
    return *this;
  }

  line_iterator operator++(int) {
    auto copy(*this);
    ++*this;
    return copy;
  }

  friend bool operator==(const line_iterator& x, const line_iterator& y) {
    return x.input_ == y.input_;
  }

  friend bool operator!=(const line_iterator& x, const line_iterator& y) {
    return !(x == y);
  }

 private:
  std::istream* input_;
  value_type s_;
};

struct lines {
  lines(std::istream& input): input_(input) {}

  auto begin() const { return line_iterator(input_); }
  auto end() const { return line_iterator(); }

 private:
  std::istream& input_;
};

#endif