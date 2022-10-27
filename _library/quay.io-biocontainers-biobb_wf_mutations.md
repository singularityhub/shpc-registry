---
layout: container
name:  "quay.io/biocontainers/biobb_wf_mutations"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_wf_mutations/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_wf_mutations/container.yaml"
updated_at: "2022-10-27 00:54:45.935388"
latest: "0.0.6--py_0"
container_url: "https://biocontainers.pro/tools/biobb_wf_mutations"
aliases:
 - ".biobb_wf_mutations-post-link.sh"
 - "GMXRC"
 - "GMXRC.bash"
 - "GMXRC.csh"
 - "GMXRC.zsh"
 - "demux.pl"
 - "editconf"
 - "fix_side_chain"
 - "genion"
 - "genrestr"
 - "gmx"
 - "gmx-completion-gmx.bash"
 - "gmx-completion.bash"
 - "grompp"
 - "hwloc-gather-cpuid"
 - "make_ndx"
 - "mdrun"
 - "mutate"
 - "ndx2resttop"
 - "pdb"
 - "pdb2gmx"
 - "pdb_cluster_zip"
 - "pdb_variants"
 - "solvate"
 - "xplor2gmx.pl"
versions:
 - "0.0.6--py_0"
description: "shpc-registry automated BioContainers addition for biobb_wf_mutations"
config: {"url": "https://biocontainers.pro/tools/biobb_wf_mutations", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_wf_mutations", "latest": {"0.0.6--py_0": "sha256:d8c4be020cfa729de2c4a18a0369789b68a3ef48994f91aa87a6b7d7502735a5"}, "tags": {"0.0.6--py_0": "sha256:d8c4be020cfa729de2c4a18a0369789b68a3ef48994f91aa87a6b7d7502735a5"}, "docker": "quay.io/biocontainers/biobb_wf_mutations", "aliases": {".biobb_wf_mutations-post-link.sh": "/usr/local/bin/.biobb_wf_mutations-post-link.sh", "GMXRC": "/usr/local/bin/GMXRC", "GMXRC.bash": "/usr/local/bin/GMXRC.bash", "GMXRC.csh": "/usr/local/bin/GMXRC.csh", "GMXRC.zsh": "/usr/local/bin/GMXRC.zsh", "demux.pl": "/usr/local/bin/demux.pl", "editconf": "/usr/local/bin/editconf", "fix_side_chain": "/usr/local/bin/fix_side_chain", "genion": "/usr/local/bin/genion", "genrestr": "/usr/local/bin/genrestr", "gmx": "/usr/local/bin/gmx", "gmx-completion-gmx.bash": "/usr/local/bin/gmx-completion-gmx.bash", "gmx-completion.bash": "/usr/local/bin/gmx-completion.bash", "grompp": "/usr/local/bin/grompp", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "make_ndx": "/usr/local/bin/make_ndx", "mdrun": "/usr/local/bin/mdrun", "mutate": "/usr/local/bin/mutate", "ndx2resttop": "/usr/local/bin/ndx2resttop", "pdb": "/usr/local/bin/pdb", "pdb2gmx": "/usr/local/bin/pdb2gmx", "pdb_cluster_zip": "/usr/local/bin/pdb_cluster_zip", "pdb_variants": "/usr/local/bin/pdb_variants", "solvate": "/usr/local/bin/solvate", "xplor2gmx.pl": "/usr/local/bin/xplor2gmx.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_wf_mutations.
shpc-registry automated BioContainers addition for biobb_wf_mutations
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_wf_mutations
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_wf_mutations:0.0.6--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_wf_mutations/0.0.6--py_0
$ module help quay.io/biocontainers/biobb_wf_mutations/0.0.6--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_wf_mutations-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_wf_mutations-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_wf_mutations-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_wf_mutations-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_wf_mutations-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_wf_mutations-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .biobb_wf_mutations-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.biobb_wf_mutations-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.biobb_wf_mutations-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.biobb_wf_mutations-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GMXRC

```bash
$ singularity exec <container> /usr/local/bin/GMXRC
$ podman run --it --rm --entrypoint /usr/local/bin/GMXRC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMXRC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GMXRC.bash

```bash
$ singularity exec <container> /usr/local/bin/GMXRC.bash
$ podman run --it --rm --entrypoint /usr/local/bin/GMXRC.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMXRC.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GMXRC.csh

```bash
$ singularity exec <container> /usr/local/bin/GMXRC.csh
$ podman run --it --rm --entrypoint /usr/local/bin/GMXRC.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMXRC.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GMXRC.zsh

```bash
$ singularity exec <container> /usr/local/bin/GMXRC.zsh
$ podman run --it --rm --entrypoint /usr/local/bin/GMXRC.zsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMXRC.zsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demux.pl

```bash
$ singularity exec <container> /usr/local/bin/demux.pl
$ podman run --it --rm --entrypoint /usr/local/bin/demux.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demux.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### editconf

```bash
$ singularity exec <container> /usr/local/bin/editconf
$ podman run --it --rm --entrypoint /usr/local/bin/editconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/editconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_side_chain

```bash
$ singularity exec <container> /usr/local/bin/fix_side_chain
$ podman run --it --rm --entrypoint /usr/local/bin/fix_side_chain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_side_chain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genion

```bash
$ singularity exec <container> /usr/local/bin/genion
$ podman run --it --rm --entrypoint /usr/local/bin/genion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genrestr

```bash
$ singularity exec <container> /usr/local/bin/genrestr
$ podman run --it --rm --entrypoint /usr/local/bin/genrestr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genrestr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmx

```bash
$ singularity exec <container> /usr/local/bin/gmx
$ podman run --it --rm --entrypoint /usr/local/bin/gmx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmx-completion-gmx.bash

```bash
$ singularity exec <container> /usr/local/bin/gmx-completion-gmx.bash
$ podman run --it --rm --entrypoint /usr/local/bin/gmx-completion-gmx.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmx-completion-gmx.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmx-completion.bash

```bash
$ singularity exec <container> /usr/local/bin/gmx-completion.bash
$ podman run --it --rm --entrypoint /usr/local/bin/gmx-completion.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmx-completion.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grompp

```bash
$ singularity exec <container> /usr/local/bin/grompp
$ podman run --it --rm --entrypoint /usr/local/bin/grompp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grompp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_ndx

```bash
$ singularity exec <container> /usr/local/bin/make_ndx
$ podman run --it --rm --entrypoint /usr/local/bin/make_ndx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_ndx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mdrun

```bash
$ singularity exec <container> /usr/local/bin/mdrun
$ podman run --it --rm --entrypoint /usr/local/bin/mdrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutate

```bash
$ singularity exec <container> /usr/local/bin/mutate
$ podman run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ndx2resttop

```bash
$ singularity exec <container> /usr/local/bin/ndx2resttop
$ podman run --it --rm --entrypoint /usr/local/bin/ndx2resttop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ndx2resttop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb

```bash
$ singularity exec <container> /usr/local/bin/pdb
$ podman run --it --rm --entrypoint /usr/local/bin/pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb2gmx

```bash
$ singularity exec <container> /usr/local/bin/pdb2gmx
$ podman run --it --rm --entrypoint /usr/local/bin/pdb2gmx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb2gmx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb_cluster_zip

```bash
$ singularity exec <container> /usr/local/bin/pdb_cluster_zip
$ podman run --it --rm --entrypoint /usr/local/bin/pdb_cluster_zip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb_cluster_zip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb_variants

```bash
$ singularity exec <container> /usr/local/bin/pdb_variants
$ podman run --it --rm --entrypoint /usr/local/bin/pdb_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### solvate

```bash
$ singularity exec <container> /usr/local/bin/solvate
$ podman run --it --rm --entrypoint /usr/local/bin/solvate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/solvate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xplor2gmx.pl

```bash
$ singularity exec <container> /usr/local/bin/xplor2gmx.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xplor2gmx.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xplor2gmx.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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