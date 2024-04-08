---
layout: container
name:  "quay.io/biocontainers/phantompeakqualtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phantompeakqualtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phantompeakqualtools/container.yaml"
updated_at: "2024-04-08 02:35:30.081615"
latest: "1.2.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/phantompeakqualtools"
aliases:
 - "run_spp.R"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "f2py3.9"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
versions:
 - "1.2.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for phantompeakqualtools"
config: {"url": "https://biocontainers.pro/tools/phantompeakqualtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phantompeakqualtools", "latest": {"1.2.2--hdfd78af_1": "sha256:ad08ef789f67575aa3bb0cca5970dbddace8180121b0205da8e2da5dd1ee5846"}, "tags": {"1.2.2--hdfd78af_1": "sha256:ad08ef789f67575aa3bb0cca5970dbddace8180121b0205da8e2da5dd1ee5846"}, "docker": "quay.io/biocontainers/phantompeakqualtools", "aliases": {"run_spp.R": "/usr/local/bin/run_spp.R", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "f2py3.9": "/usr/local/bin/f2py3.9", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phantompeakqualtools.
shpc-registry automated BioContainers addition for phantompeakqualtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phantompeakqualtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phantompeakqualtools:1.2.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phantompeakqualtools/1.2.2--hdfd78af_1
$ module help quay.io/biocontainers/phantompeakqualtools/1.2.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phantompeakqualtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phantompeakqualtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phantompeakqualtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phantompeakqualtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phantompeakqualtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phantompeakqualtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### run_spp.R

```bash
$ singularity exec <container> /usr/local/bin/run_spp.R
$ podman run --it --rm --entrypoint /usr/local/bin/run_spp.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_spp.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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