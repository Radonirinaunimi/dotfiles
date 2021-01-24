#!/usr/bin/env bash

vim $(fzf --preview 'bat --color "always" {}')
