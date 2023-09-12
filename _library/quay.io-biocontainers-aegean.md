---
layout: container
name:  "quay.io/biocontainers/aegean"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aegean/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aegean/container.yaml"
updated_at: "2023-09-12 02:56:28.660717"
latest: "0.16.0--hc3aac3a_4"
container_url: "https://biocontainers.pro/tools/aegean"
aliases:
 - "canon-gff3"
 - "gaeval"
 - "genometools-config"
 - "gt"
 - "locuspocus"
 - "parseval"
 - "pmrna"
 - "tidygff3"
 - "xtractore"
 - "git"
 - "git-cvsserver"
 - "git-receive-pack"
 - "git-shell"
 - "git-upload-archive"
 - "git-upload-pack"
 - "gitk"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
versions:
 - "0.16.0--hde46a50_3"
 - "0.16.0--hc3aac3a_4"
description: "shpc-registry automated BioContainers addition for aegean"
config: {"url": "https://biocontainers.pro/tools/aegean", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aegean", "latest": {"0.16.0--hc3aac3a_4": "sha256:a9919f2cf6f9b2556b92028b9cf8989130c0f24712ca8886f3ee8b7f6b5c527b"}, "tags": {"0.16.0--hde46a50_3": "sha256:3c0b843f958647204a367e1812ce9a9570a776e74d4285a8aeb6be456f158858", "0.16.0--hc3aac3a_4": "sha256:a9919f2cf6f9b2556b92028b9cf8989130c0f24712ca8886f3ee8b7f6b5c527b"}, "docker": "quay.io/biocontainers/aegean", "aliases": {"canon-gff3": "/usr/local/bin/canon-gff3", "gaeval": "/usr/local/bin/gaeval", "genometools-config": "/usr/local/bin/genometools-config", "gt": "/usr/local/bin/gt", "locuspocus": "/usr/local/bin/locuspocus", "parseval": "/usr/local/bin/parseval", "pmrna": "/usr/local/bin/pmrna", "tidygff3": "/usr/local/bin/tidygff3", "xtractore": "/usr/local/bin/xtractore", "git": "/usr/local/bin/git", "git-cvsserver": "/usr/local/bin/git-cvsserver", "git-receive-pack": "/usr/local/bin/git-receive-pack", "git-shell": "/usr/local/bin/git-shell", "git-upload-archive": "/usr/local/bin/git-upload-archive", "git-upload-pack": "/usr/local/bin/git-upload-pack", "gitk": "/usr/local/bin/gitk", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aegean.
shpc-registry automated BioContainers addition for aegean
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aegean
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aegean:0.16.0--hc3aac3a_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aegean/0.16.0--hc3aac3a_4
$ module help quay.io/biocontainers/aegean/0.16.0--hc3aac3a_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aegean-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aegean-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aegean-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aegean-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aegean-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aegean-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### canon-gff3

```bash
$ singularity exec <container> /usr/local/bin/canon-gff3
$ podman run --it --rm --entrypoint /usr/local/bin/canon-gff3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canon-gff3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gaeval

```bash
$ singularity exec <container> /usr/local/bin/gaeval
$ podman run --it --rm --entrypoint /usr/local/bin/gaeval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gaeval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genometools-config

```bash
$ singularity exec <container> /usr/local/bin/genometools-config
$ podman run --it --rm --entrypoint /usr/local/bin/genometools-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genometools-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gt

```bash
$ singularity exec <container> /usr/local/bin/gt
$ podman run --it --rm --entrypoint /usr/local/bin/gt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locuspocus

```bash
$ singularity exec <container> /usr/local/bin/locuspocus
$ podman run --it --rm --entrypoint /usr/local/bin/locuspocus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locuspocus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parseval

```bash
$ singularity exec <container> /usr/local/bin/parseval
$ podman run --it --rm --entrypoint /usr/local/bin/parseval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parseval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmrna

```bash
$ singularity exec <container> /usr/local/bin/pmrna
$ podman run --it --rm --entrypoint /usr/local/bin/pmrna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmrna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tidygff3

```bash
$ singularity exec <container> /usr/local/bin/tidygff3
$ podman run --it --rm --entrypoint /usr/local/bin/tidygff3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tidygff3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtractore

```bash
$ singularity exec <container> /usr/local/bin/xtractore
$ podman run --it --rm --entrypoint /usr/local/bin/xtractore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtractore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git

```bash
$ singularity exec <container> /usr/local/bin/git
$ podman run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-cvsserver

```bash
$ singularity exec <container> /usr/local/bin/git-cvsserver
$ podman run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-receive-pack

```bash
$ singularity exec <container> /usr/local/bin/git-receive-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-shell

```bash
$ singularity exec <container> /usr/local/bin/git-shell
$ podman run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-archive

```bash
$ singularity exec <container> /usr/local/bin/git-upload-archive
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-pack

```bash
$ singularity exec <container> /usr/local/bin/git-upload-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gitk

```bash
$ singularity exec <container> /usr/local/bin/gitk
$ podman run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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