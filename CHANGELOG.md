# Changelog

All notable changes to this collection will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- Ansible Galaxy publish workflow, pre-commit hooks, and argument specs for the `mssql` and `patch` roles.

### Changed

- `galaxy.yml` version is the `0.0.0-semantic-version` placeholder substituted at publish time. A commit message containing `#major` or `#minor` bumps that component; otherwise the workflow increments the patch version.
- Collection metadata now requires Ansible `>=2.15.0`.
- SQL service accounts are created with `microsoft.ad.user`. `community.windows.win_domain_user` was removed in community.windows 3.0.0.
- READMEs match the role argument specs and the `smb_info` module documentation.

## [1.0.1] and earlier

Releases prior to this file being introduced were tracked only via [GitHub tags](https://github.com/autodotes/zjleblanc.windows/tags) and commit history.
