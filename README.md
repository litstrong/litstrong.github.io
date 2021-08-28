# Build production Jekyll html

JEKYLL_ENV=production bundle exec jekyll build

Note that after switching to Apple M1, I need to use below command:

JEKYLL_ENV=production arch -arch x86_64 bundle exec jekyll serve

Details see:
https://github.com/ffi/ffi/issues/870
