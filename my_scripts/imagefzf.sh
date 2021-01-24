#!/usr/bin/env bash

sxiv $(fzf --preview 'bat --color "always" {}')
