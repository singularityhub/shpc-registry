---
layout: container
name:  "quay.io/biocontainers/matchtigs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/matchtigs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/matchtigs/container.yaml"
updated_at: "2024-10-17 03:20:38.019585"
latest: "2.1.7--h715e4b3_1"
container_url: "https://biocontainers.pro/tools/matchtigs"
aliases:
 - "cargo"
 - "cargo-clippy"
 - "cargo-fmt"
 - "clippy-driver"
 - "matchtigs"
 - "rls"
 - "rust-demangler"
 - "rust-gdb"
 - "rust-gdbgui"
 - "rust-lldb"
 - "rustc"
 - "rustdoc"
 - "rustfmt"
versions:
 - "1.2.0--hdfd78af_0"
 - "1.5.3--hec16e2b_0"
 - "1.3.1--hdfd78af_0"
 - "1.5.5--hec16e2b_0"
 - "2.1.5--h031d066_0"
 - "2.1.7--h715e4b3_1"
description: "shpc-registry automated BioContainers addition for matchtigs"
config: {"url": "https://biocontainers.pro/tools/matchtigs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for matchtigs", "latest": {"2.1.7--h715e4b3_1": "sha256:7b7c20a4009d3486f0644b37175365f5071c93b5ceb7aecec8d177651472137a"}, "tags": {"1.2.0--hdfd78af_0": "sha256:f35cc56c7409188e63259484d4f5f9db116c4b808d56d521fcf62ffc67a24647", "1.5.3--hec16e2b_0": "sha256:a473015e335da9771d76e5187185fa06dd76fc8ff14fa594dbf0cb7c3a3069df", "1.3.1--hdfd78af_0": "sha256:a7eec4dc83a5cb18a7547b988510b5bdac3b809ec1f857525a271f9bebc938fa", "1.5.5--hec16e2b_0": "sha256:c1eb21aec5191a05f2fb28d652f1277f192807c6069546567879dcd3367ffe18", "2.1.5--h031d066_0": "sha256:389a81e545e041247c44adab0368e6f021e6c00f9d340fee9c9ec916e4c81eff", "2.1.7--h715e4b3_1": "sha256:7b7c20a4009d3486f0644b37175365f5071c93b5ceb7aecec8d177651472137a"}, "docker": "quay.io/biocontainers/matchtigs", "aliases": {"cargo": "/usr/local/bin/cargo", "cargo-clippy": "/usr/local/bin/cargo-clippy", "cargo-fmt": "/usr/local/bin/cargo-fmt", "clippy-driver": "/usr/local/bin/clippy-driver", "matchtigs": "/usr/local/bin/matchtigs", "rls": "/usr/local/bin/rls", "rust-demangler": "/usr/local/bin/rust-demangler", "rust-gdb": "/usr/local/bin/rust-gdb", "rust-gdbgui": "/usr/local/bin/rust-gdbgui", "rust-lldb": "/usr/local/bin/rust-lldb", "rustc": "/usr/local/bin/rustc", "rustdoc": "/usr/local/bin/rustdoc", "rustfmt": "/usr/local/bin/rustfmt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/matchtigs.
shpc-registry automated BioContainers addition for matchtigs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/matchtigs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/matchtigs:2.1.7--h715e4b3_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/matchtigs/2.1.7--h715e4b3_1
$ module help quay.io/biocontainers/matchtigs/2.1.7--h715e4b3_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### matchtigs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### matchtigs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### matchtigs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### matchtigs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### matchtigs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### matchtigs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cargo

```bash
$ singularity exec <container> /usr/local/bin/cargo
$ podman run --it --rm --entrypoint /usr/local/bin/cargo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cargo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cargo-clippy

```bash
$ singularity exec <container> /usr/local/bin/cargo-clippy
$ podman run --it --rm --entrypoint /usr/local/bin/cargo-clippy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cargo-clippy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cargo-fmt

```bash
$ singularity exec <container> /usr/local/bin/cargo-fmt
$ podman run --it --rm --entrypoint /usr/local/bin/cargo-fmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cargo-fmt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clippy-driver

```bash
$ singularity exec <container> /usr/local/bin/clippy-driver
$ podman run --it --rm --entrypoint /usr/local/bin/clippy-driver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clippy-driver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matchtigs

```bash
$ singularity exec <container> /usr/local/bin/matchtigs
$ podman run --it --rm --entrypoint /usr/local/bin/matchtigs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matchtigs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rls

```bash
$ singularity exec <container> /usr/local/bin/rls
$ podman run --it --rm --entrypoint /usr/local/bin/rls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust-demangler

```bash
$ singularity exec <container> /usr/local/bin/rust-demangler
$ podman run --it --rm --entrypoint /usr/local/bin/rust-demangler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust-demangler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust-gdb

```bash
$ singularity exec <container> /usr/local/bin/rust-gdb
$ podman run --it --rm --entrypoint /usr/local/bin/rust-gdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust-gdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust-gdbgui

```bash
$ singularity exec <container> /usr/local/bin/rust-gdbgui
$ podman run --it --rm --entrypoint /usr/local/bin/rust-gdbgui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust-gdbgui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rust-lldb

```bash
$ singularity exec <container> /usr/local/bin/rust-lldb
$ podman run --it --rm --entrypoint /usr/local/bin/rust-lldb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust-lldb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rustc

```bash
$ singularity exec <container> /usr/local/bin/rustc
$ podman run --it --rm --entrypoint /usr/local/bin/rustc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rustc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rustdoc

```bash
$ singularity exec <container> /usr/local/bin/rustdoc
$ podman run --it --rm --entrypoint /usr/local/bin/rustdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rustdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rustfmt

```bash
$ singularity exec <container> /usr/local/bin/rustfmt
$ podman run --it --rm --entrypoint /usr/local/bin/rustfmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rustfmt   -v ${PWD} -w ${PWD} <container> -c " $@"
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