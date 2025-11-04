---
layout: container
name:  "quay.io/biocontainers/phylocsf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylocsf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phylocsf/container.yaml"
updated_at: "2025-11-04 03:39:16.931300"
latest: "1.0.1--h3eba124_1"
container_url: "https://biocontainers.pro/tools/phylocsf"
aliases:
 - "PhyloCSF"
 - "PhyloCSF.Linux.x86_64"
 - "ocaml"
 - "ocamlc"
 - "ocamlc.byte"
 - "ocamlc.opt"
 - "ocamlcmt"
 - "ocamlcp"
 - "ocamlcp.byte"
 - "ocamlcp.opt"
 - "ocamldebug"
 - "ocamldep"
 - "ocamldep.byte"
 - "ocamldep.opt"
 - "ocamldoc"
 - "ocamldoc.opt"
 - "ocamllex"
 - "ocamllex.byte"
 - "ocamllex.opt"
 - "ocamlmklib"
 - "ocamlmklib.byte"
 - "ocamlmklib.opt"
 - "ocamlmktop"
 - "ocamlmktop.byte"
 - "ocamlmktop.opt"
 - "ocamlobjinfo"
 - "ocamlobjinfo.byte"
 - "ocamlobjinfo.opt"
 - "ocamlopt"
 - "ocamlopt.byte"
 - "ocamlopt.opt"
 - "ocamloptp"
 - "ocamloptp.byte"
 - "ocamloptp.opt"
 - "ocamlprof"
 - "ocamlprof.byte"
 - "ocamlprof.opt"
 - "ocamlrun"
 - "ocamlyacc"
 - "c89"
 - "c99"
versions:
 - "1.0.1--h3eba124_1"
description: "shpc-registry automated BioContainers addition for phylocsf"
config: {"url": "https://biocontainers.pro/tools/phylocsf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylocsf", "latest": {"1.0.1--h3eba124_1": "sha256:416bb1f7e1fade714091dfea775f7a9d4f4a4c1bada91d0747ae4e3caa3bcd91"}, "tags": {"1.0.1--h3eba124_1": "sha256:416bb1f7e1fade714091dfea775f7a9d4f4a4c1bada91d0747ae4e3caa3bcd91"}, "docker": "quay.io/biocontainers/phylocsf", "aliases": {"PhyloCSF": "/usr/local/bin/PhyloCSF", "PhyloCSF.Linux.x86_64": "/usr/local/bin/PhyloCSF.Linux.x86_64", "ocaml": "/usr/local/bin/ocaml", "ocamlc": "/usr/local/bin/ocamlc", "ocamlc.byte": "/usr/local/bin/ocamlc.byte", "ocamlc.opt": "/usr/local/bin/ocamlc.opt", "ocamlcmt": "/usr/local/bin/ocamlcmt", "ocamlcp": "/usr/local/bin/ocamlcp", "ocamlcp.byte": "/usr/local/bin/ocamlcp.byte", "ocamlcp.opt": "/usr/local/bin/ocamlcp.opt", "ocamldebug": "/usr/local/bin/ocamldebug", "ocamldep": "/usr/local/bin/ocamldep", "ocamldep.byte": "/usr/local/bin/ocamldep.byte", "ocamldep.opt": "/usr/local/bin/ocamldep.opt", "ocamldoc": "/usr/local/bin/ocamldoc", "ocamldoc.opt": "/usr/local/bin/ocamldoc.opt", "ocamllex": "/usr/local/bin/ocamllex", "ocamllex.byte": "/usr/local/bin/ocamllex.byte", "ocamllex.opt": "/usr/local/bin/ocamllex.opt", "ocamlmklib": "/usr/local/bin/ocamlmklib", "ocamlmklib.byte": "/usr/local/bin/ocamlmklib.byte", "ocamlmklib.opt": "/usr/local/bin/ocamlmklib.opt", "ocamlmktop": "/usr/local/bin/ocamlmktop", "ocamlmktop.byte": "/usr/local/bin/ocamlmktop.byte", "ocamlmktop.opt": "/usr/local/bin/ocamlmktop.opt", "ocamlobjinfo": "/usr/local/bin/ocamlobjinfo", "ocamlobjinfo.byte": "/usr/local/bin/ocamlobjinfo.byte", "ocamlobjinfo.opt": "/usr/local/bin/ocamlobjinfo.opt", "ocamlopt": "/usr/local/bin/ocamlopt", "ocamlopt.byte": "/usr/local/bin/ocamlopt.byte", "ocamlopt.opt": "/usr/local/bin/ocamlopt.opt", "ocamloptp": "/usr/local/bin/ocamloptp", "ocamloptp.byte": "/usr/local/bin/ocamloptp.byte", "ocamloptp.opt": "/usr/local/bin/ocamloptp.opt", "ocamlprof": "/usr/local/bin/ocamlprof", "ocamlprof.byte": "/usr/local/bin/ocamlprof.byte", "ocamlprof.opt": "/usr/local/bin/ocamlprof.opt", "ocamlrun": "/usr/local/bin/ocamlrun", "ocamlyacc": "/usr/local/bin/ocamlyacc", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylocsf.
shpc-registry automated BioContainers addition for phylocsf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylocsf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylocsf:1.0.1--h3eba124_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylocsf/1.0.1--h3eba124_1
$ module help quay.io/biocontainers/phylocsf/1.0.1--h3eba124_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylocsf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylocsf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylocsf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylocsf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylocsf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylocsf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PhyloCSF

```bash
$ singularity exec <container> /usr/local/bin/PhyloCSF
$ podman run --it --rm --entrypoint /usr/local/bin/PhyloCSF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PhyloCSF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PhyloCSF.Linux.x86_64

```bash
$ singularity exec <container> /usr/local/bin/PhyloCSF.Linux.x86_64
$ podman run --it --rm --entrypoint /usr/local/bin/PhyloCSF.Linux.x86_64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PhyloCSF.Linux.x86_64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocaml

```bash
$ singularity exec <container> /usr/local/bin/ocaml
$ podman run --it --rm --entrypoint /usr/local/bin/ocaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlc

```bash
$ singularity exec <container> /usr/local/bin/ocamlc
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlc.byte

```bash
$ singularity exec <container> /usr/local/bin/ocamlc.byte
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlc.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlc.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlc.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamlc.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlc.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlc.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlcmt

```bash
$ singularity exec <container> /usr/local/bin/ocamlcmt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlcmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlcmt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlcp

```bash
$ singularity exec <container> /usr/local/bin/ocamlcp
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlcp.byte

```bash
$ singularity exec <container> /usr/local/bin/ocamlcp.byte
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlcp.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlcp.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlcp.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamlcp.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlcp.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlcp.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamldebug

```bash
$ singularity exec <container> /usr/local/bin/ocamldebug
$ podman run --it --rm --entrypoint /usr/local/bin/ocamldebug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamldebug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamldep

```bash
$ singularity exec <container> /usr/local/bin/ocamldep
$ podman run --it --rm --entrypoint /usr/local/bin/ocamldep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamldep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamldep.byte

```bash
$ singularity exec <container> /usr/local/bin/ocamldep.byte
$ podman run --it --rm --entrypoint /usr/local/bin/ocamldep.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamldep.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamldep.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamldep.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamldep.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamldep.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamldoc

```bash
$ singularity exec <container> /usr/local/bin/ocamldoc
$ podman run --it --rm --entrypoint /usr/local/bin/ocamldoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamldoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamldoc.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamldoc.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamldoc.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamldoc.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamllex

```bash
$ singularity exec <container> /usr/local/bin/ocamllex
$ podman run --it --rm --entrypoint /usr/local/bin/ocamllex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamllex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamllex.byte

```bash
$ singularity exec <container> /usr/local/bin/ocamllex.byte
$ podman run --it --rm --entrypoint /usr/local/bin/ocamllex.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamllex.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamllex.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamllex.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamllex.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamllex.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlmklib

```bash
$ singularity exec <container> /usr/local/bin/ocamlmklib
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlmklib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlmklib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlmklib.byte

```bash
$ singularity exec <container> /usr/local/bin/ocamlmklib.byte
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlmklib.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlmklib.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlmklib.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamlmklib.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlmklib.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlmklib.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlmktop

```bash
$ singularity exec <container> /usr/local/bin/ocamlmktop
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlmktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlmktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlmktop.byte

```bash
$ singularity exec <container> /usr/local/bin/ocamlmktop.byte
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlmktop.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlmktop.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlmktop.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamlmktop.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlmktop.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlmktop.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlobjinfo

```bash
$ singularity exec <container> /usr/local/bin/ocamlobjinfo
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlobjinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlobjinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlobjinfo.byte

```bash
$ singularity exec <container> /usr/local/bin/ocamlobjinfo.byte
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlobjinfo.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlobjinfo.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlobjinfo.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamlobjinfo.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlobjinfo.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlobjinfo.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlopt

```bash
$ singularity exec <container> /usr/local/bin/ocamlopt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlopt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlopt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlopt.byte

```bash
$ singularity exec <container> /usr/local/bin/ocamlopt.byte
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlopt.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlopt.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlopt.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamlopt.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlopt.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlopt.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamloptp

```bash
$ singularity exec <container> /usr/local/bin/ocamloptp
$ podman run --it --rm --entrypoint /usr/local/bin/ocamloptp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamloptp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamloptp.byte

```bash
$ singularity exec <container> /usr/local/bin/ocamloptp.byte
$ podman run --it --rm --entrypoint /usr/local/bin/ocamloptp.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamloptp.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamloptp.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamloptp.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamloptp.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamloptp.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlprof

```bash
$ singularity exec <container> /usr/local/bin/ocamlprof
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlprof.byte

```bash
$ singularity exec <container> /usr/local/bin/ocamlprof.byte
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlprof.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlprof.byte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlprof.opt

```bash
$ singularity exec <container> /usr/local/bin/ocamlprof.opt
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlprof.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlprof.opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlrun

```bash
$ singularity exec <container> /usr/local/bin/ocamlrun
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocamlyacc

```bash
$ singularity exec <container> /usr/local/bin/ocamlyacc
$ podman run --it --rm --entrypoint /usr/local/bin/ocamlyacc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocamlyacc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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