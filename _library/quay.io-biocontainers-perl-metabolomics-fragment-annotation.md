---
layout: container
name:  "quay.io/biocontainers/perl-metabolomics-fragment-annotation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-metabolomics-fragment-annotation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-metabolomics-fragment-annotation/container.yaml"
updated_at: "2024-07-11 03:23:55.359201"
latest: "0.6.9--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-metabolomics-fragment-annotation"
aliases:
 - "xml_grep"
 - "xml_merge"
 - "xml_pp"
 - "xml_spellcheck"
 - "xml_split"
 - "webtidy"
 - "tidyp"
 - "htmltree"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.6.3--pl5321hdfd78af_2"
 - "0.6.9--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-metabolomics-fragment-annotation"
config: {"url": "https://biocontainers.pro/tools/perl-metabolomics-fragment-annotation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-metabolomics-fragment-annotation", "latest": {"0.6.9--pl5321hdfd78af_0": "sha256:af06699f4df8732a235a4335ed937f8c2112980c57a5db0d87dcf810894a00dd"}, "tags": {"0.6.3--pl5321hdfd78af_2": "sha256:0c1524638e6ba92ef2160098e868a43abaca29c72696e03a0fec4446322d55a3", "0.6.9--pl5321hdfd78af_0": "sha256:af06699f4df8732a235a4335ed937f8c2112980c57a5db0d87dcf810894a00dd"}, "docker": "quay.io/biocontainers/perl-metabolomics-fragment-annotation", "aliases": {"xml_grep": "/usr/local/bin/xml_grep", "xml_merge": "/usr/local/bin/xml_merge", "xml_pp": "/usr/local/bin/xml_pp", "xml_spellcheck": "/usr/local/bin/xml_spellcheck", "xml_split": "/usr/local/bin/xml_split", "webtidy": "/usr/local/bin/webtidy", "tidyp": "/usr/local/bin/tidyp", "htmltree": "/usr/local/bin/htmltree", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-metabolomics-fragment-annotation.
shpc-registry automated BioContainers addition for perl-metabolomics-fragment-annotation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-metabolomics-fragment-annotation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-metabolomics-fragment-annotation:0.6.9--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-metabolomics-fragment-annotation/0.6.9--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-metabolomics-fragment-annotation/0.6.9--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-metabolomics-fragment-annotation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-metabolomics-fragment-annotation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-metabolomics-fragment-annotation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-metabolomics-fragment-annotation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-metabolomics-fragment-annotation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-metabolomics-fragment-annotation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xml_grep

```bash
$ singularity exec <container> /usr/local/bin/xml_grep
$ podman run --it --rm --entrypoint /usr/local/bin/xml_grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_merge

```bash
$ singularity exec <container> /usr/local/bin/xml_merge
$ podman run --it --rm --entrypoint /usr/local/bin/xml_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_pp

```bash
$ singularity exec <container> /usr/local/bin/xml_pp
$ podman run --it --rm --entrypoint /usr/local/bin/xml_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_spellcheck

```bash
$ singularity exec <container> /usr/local/bin/xml_spellcheck
$ podman run --it --rm --entrypoint /usr/local/bin/xml_spellcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_spellcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_split

```bash
$ singularity exec <container> /usr/local/bin/xml_split
$ podman run --it --rm --entrypoint /usr/local/bin/xml_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### webtidy

```bash
$ singularity exec <container> /usr/local/bin/webtidy
$ podman run --it --rm --entrypoint /usr/local/bin/webtidy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/webtidy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tidyp

```bash
$ singularity exec <container> /usr/local/bin/tidyp
$ podman run --it --rm --entrypoint /usr/local/bin/tidyp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tidyp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htmltree

```bash
$ singularity exec <container> /usr/local/bin/htmltree
$ podman run --it --rm --entrypoint /usr/local/bin/htmltree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htmltree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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