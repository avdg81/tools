@echo off

REM A small script to resemble the `config` alias as described by the article
REM "Dotfiles: Best way to store in a bare git repository"
REM (https://www.atlassian.com/git/tutorials/dotfiles)
git --git-dir=%HOMEDRIVE%%HOMEPATH%\.cfg\ --work-tree=%HOMEDRIVE%%HOMEPATH% %*
