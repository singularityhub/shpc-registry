---
layout: container
name:  "ghcr.io/autamus/rust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/rust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/rust/container.yaml"
updated_at: "2023-11-16 03:15:27.326065"
latest: "1.60.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/rust"
aliases:
 - "cargo"
 - "cargo-clippy"
 - "cargo-fmt"
 - "clippy-driver"
 - "rust"
 - "rust-gdb"
 - "rust-gdbgui"
 - "rust-lldb"
 - "rustc"
 - "rustdoc"
 - "rustfmt"
versions:
 - "1.50.0"
 - "1.52.1"
 - "1.53.0"
 - "1.54.0"
 - "latest"
 - "1.60.0"
description: "Rust is a multi-paradigm programming language designed for performance and safety, especially safe concurrency."
config: {"docker": "ghcr.io/autamus/rust", "url": "https://github.com/orgs/autamus/packages/container/package/rust", "maintainer": "@vsoch", "description": "Rust is a multi-paradigm programming language designed for performance and safety, especially safe concurrency.", "latest": {"1.60.0": "sha256:f70aa1c2a1556226ba21c1aa70ead168e91ac0824225edafced369de9a48f6e0"}, "tags": {"1.50.0": "sha256:238c8e6fd628cea11f9023ab4b92b1e1295cae1400548b318c62fbe9be616611", "1.52.1": "sha256:340e767aa1f43b61f2ffbce26072e4846b2068c73b4808eb85f8cf9f4630d24a", "1.53.0": "sha256:ee8420808012967a81d5a205dee5372134e2b0ee63a1729d8b8550d91e823ba1", "1.54.0": "sha256:df047336872fe0ffae5ee3f683e166cd816d7a6a437ddc63de6d19a5c9e713c9", "latest": "sha256:f70aa1c2a1556226ba21c1aa70ead168e91ac0824225edafced369de9a48f6e0", "1.60.0": "sha256:f70aa1c2a1556226ba21c1aa70ead168e91ac0824225edafced369de9a48f6e0"}, "aliases": {"cargo": "/opt/view/bin/cargo", "cargo-clippy": "/opt/view/bin/cargo-clippy", "cargo-fmt": "/opt/view/bin/cargo-fmt", "clippy-driver": "/opt/view/bin/clippy-driver", "rust": "/opt/view/bin/rust", "rust-gdb": "/opt/view/bin/rust-gdb", "rust-gdbgui": "/opt/view/bin/rust-gdbgui", "rust-lldb": "/opt/view/bin/rust-lldb", "rustc": "/opt/view/bin/rustc", "rustdoc": "/opt/view/bin/rustdoc", "rustfmt": "/opt/view/bin/rustfmt"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/rust.
Rust is a multi-paradigm programming language designed for performance and safety, especially safe concurrency.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/rust
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/rust:1.60.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/rust/1.60.0
$ module help ghcr.io/autamus/rust/1.60.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cargo

```bash
$ singularity exec <container> /opt/view/bin/cargo
$ podman run --it --rm --entrypoint /opt/view/bin/cargo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cargo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cargo-clippy

```bash
$ singularity exec <container> /opt/view/bin/cargo-clippy
$ podman run --it --rm --entrypoint /opt/view/bin/cargo-clippy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cargo-clippy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cargo-fmt

```bash
$ singularity exec <container> /opt/view/bin/cargo-fmt
$ podman run --it --rm --entrypoint /opt/view/bin/cargo-fmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cargo-fmt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clippy-driver

```bash
$ singularity exec <container> /opt/view/bin/clippy-driver
$ podman run --it --rm --entrypoint /opt/view/bin/clippy-driver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/clippy-driver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust

```bash
$ singularity exec <container> /opt/view/bin/rust
$ podman run --it --rm --entrypoint /opt/view/bin/rust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust-gdb

```bash
$ singularity exec <container> /opt/view/bin/rust-gdb
$ podman run --it --rm --entrypoint /opt/view/bin/rust-gdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rust-gdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust-gdbgui

```bash
$ singularity exec <container> /opt/view/bin/rust-gdbgui
$ podman run --it --rm --entrypoint /opt/view/bin/rust-gdbgui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rust-gdbgui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust-lldb

```bash
$ singularity exec <container> /opt/view/bin/rust-lldb
$ podman run --it --rm --entrypoint /opt/view/bin/rust-lldb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rust-lldb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rustc

```bash
$ singularity exec <container> /opt/view/bin/rustc
$ podman run --it --rm --entrypoint /opt/view/bin/rustc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rustc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rustdoc

```bash
$ singularity exec <container> /opt/view/bin/rustdoc
$ podman run --it --rm --entrypoint /opt/view/bin/rustdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rustdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rustfmt

```bash
$ singularity exec <container> /opt/view/bin/rustfmt
$ podman run --it --rm --entrypoint /opt/view/bin/rustfmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rustfmt   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)