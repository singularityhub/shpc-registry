---
layout: container
name:  "quay.io/biocontainers/tb-profiler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tb-profiler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tb-profiler/container.yaml"
updated_at: "2023-03-18 03:03:50.332646"
latest: "4.0.3--pypyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/tb-profiler"
aliases:
 - "add_dummy_AD.py"
 - "combine_vcf_variants.py"
 - "delly"
 - "rename_vcf_chrom.py"
 - "tb-profiler"
 - "gatk"
 - "tabix++"
 - "git"
 - "git-cvsserver"
 - "git-receive-pack"
 - "git-shell"
 - "git-upload-archive"
 - "git-upload-pack"
 - "gitk"
 - "plotBfst.R"
versions:
 - "4.0.3--pypyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for tb-profiler"
config: {"url": "https://biocontainers.pro/tools/tb-profiler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tb-profiler", "latest": {"4.0.3--pypyh5e36f6f_0": "sha256:68bf8f25b462196c1ae5c8b340ee7026fd69f3ae01450e8a31314f494c73d85d"}, "tags": {"4.0.3--pypyh5e36f6f_0": "sha256:68bf8f25b462196c1ae5c8b340ee7026fd69f3ae01450e8a31314f494c73d85d"}, "docker": "quay.io/biocontainers/tb-profiler", "aliases": {"add_dummy_AD.py": "/usr/local/bin/add_dummy_AD.py", "combine_vcf_variants.py": "/usr/local/bin/combine_vcf_variants.py", "delly": "/usr/local/bin/delly", "rename_vcf_chrom.py": "/usr/local/bin/rename_vcf_chrom.py", "tb-profiler": "/usr/local/bin/tb-profiler", "gatk": "/usr/local/bin/gatk", "tabix++": "/usr/local/bin/tabix++", "git": "/usr/local/bin/git", "git-cvsserver": "/usr/local/bin/git-cvsserver", "git-receive-pack": "/usr/local/bin/git-receive-pack", "git-shell": "/usr/local/bin/git-shell", "git-upload-archive": "/usr/local/bin/git-upload-archive", "git-upload-pack": "/usr/local/bin/git-upload-pack", "gitk": "/usr/local/bin/gitk", "plotBfst.R": "/usr/local/bin/plotBfst.R"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tb-profiler.
shpc-registry automated BioContainers addition for tb-profiler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tb-profiler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tb-profiler:4.0.3--pypyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tb-profiler/4.0.3--pypyh5e36f6f_0
$ module help quay.io/biocontainers/tb-profiler/4.0.3--pypyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tb-profiler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tb-profiler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tb-profiler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tb-profiler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tb-profiler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tb-profiler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_dummy_AD.py

```bash
$ singularity exec <container> /usr/local/bin/add_dummy_AD.py
$ podman run --it --rm --entrypoint /usr/local/bin/add_dummy_AD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_dummy_AD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_vcf_variants.py

```bash
$ singularity exec <container> /usr/local/bin/combine_vcf_variants.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_vcf_variants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_vcf_variants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delly

```bash
$ singularity exec <container> /usr/local/bin/delly
$ podman run --it --rm --entrypoint /usr/local/bin/delly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_vcf_chrom.py

```bash
$ singularity exec <container> /usr/local/bin/rename_vcf_chrom.py
$ podman run --it --rm --entrypoint /usr/local/bin/rename_vcf_chrom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_vcf_chrom.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tb-profiler

```bash
$ singularity exec <container> /usr/local/bin/tb-profiler
$ podman run --it --rm --entrypoint /usr/local/bin/tb-profiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tb-profiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk

```bash
$ singularity exec <container> /usr/local/bin/gatk
$ podman run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix++

```bash
$ singularity exec <container> /usr/local/bin/tabix++
$ podman run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### plotBfst.R

```bash
$ singularity exec <container> /usr/local/bin/plotBfst.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotBfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotBfst.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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