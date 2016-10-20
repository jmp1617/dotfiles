set number
set visualbell
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set textwidth=80

colorscheme blaquemagick.vim
syntax on

" This shows "bad" white spaces, i.e. white space at the end of a line or mixed
" spaces & tabs.
highlight ExtraWhitespace ctermbg=red guibg=red
autocmd Syntax * syn match ExtraWhitespace /\s\+$\| \+\ze\t/ containedin=ALL

" This switches between paste mode and normal mode when you press <F 10>.
" Paste mode makes vim do as little processing as possible on the stuff you
" input, like indenting, wrapping, etc.
set pastetoggle=<F10>

" These make it so that if you're searching in all lowercase, then it is
" done
" case insensitive.
set ignorecase smartcase

" This makes it so that all the hits for your current search is highlighted.
" Note that if you've searched but no longer want the hits to be highlighted,
" use :noh in Normal mode (short for nohlsearch) to turn them off until
" you search again, or use the bind below and press space.
set hlsearch

" This makes searching incremental, so as soon as you start typing, it
" starts searching for the currently entered text. Remember to press Enter if
" you're happy with the hit so far to move the cursor there (Esc moves
" it back to your original position).
set incsearch

set secure

set spell
