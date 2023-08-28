---
layout: container
name:  "quay.io/biocontainers/detonate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/detonate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/detonate/container.yaml"
updated_at: "2023-08-28 03:32:37.481111"
latest: "1.11--hae1ec2f_3"
container_url: "https://biocontainers.pro/tools/detonate"
aliases:
 - "ref-eval"
 - "ref-eval-estimate-true-assembly"
 - "rsem-build-read-index"
 - "rsem-eval-calculate-score"
 - "rsem-eval-estimate-transcript-length-distribution"
 - "rsem-eval-run-em"
 - "rsem-extract-reference-transcripts"
 - "rsem-parse-alignments"
 - "rsem-plot-model"
 - "rsem-preref"
 - "rsem-sam-validator"
 - "rsem-scan-for-paired-end-reads"
 - "rsem-simulate-reads"
 - "rsem-synthesis-reference-transcripts"
 - "rsem_perl_utils.pm"
 - "varfilter.py"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "perl5.26.2"
 - "ace2sam"
versions:
 - "1.11--hae1ec2f_3"
description: "shpc-registry automated BioContainers addition for detonate"
config: {"url": "https://biocontainers.pro/tools/detonate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for detonate", "latest": {"1.11--hae1ec2f_3": "sha256:709d2a47767694eadf9e19dd278e57d5f1fd23dcaf6f0889a015570ea892475f"}, "tags": {"1.11--hae1ec2f_3": "sha256:709d2a47767694eadf9e19dd278e57d5f1fd23dcaf6f0889a015570ea892475f"}, "docker": "quay.io/biocontainers/detonate", "aliases": {"ref-eval": "/usr/local/bin/ref-eval", "ref-eval-estimate-true-assembly": "/usr/local/bin/ref-eval-estimate-true-assembly", "rsem-build-read-index": "/usr/local/bin/rsem-build-read-index", "rsem-eval-calculate-score": "/usr/local/bin/rsem-eval-calculate-score", "rsem-eval-estimate-transcript-length-distribution": "/usr/local/bin/rsem-eval-estimate-transcript-length-distribution", "rsem-eval-run-em": "/usr/local/bin/rsem-eval-run-em", "rsem-extract-reference-transcripts": "/usr/local/bin/rsem-extract-reference-transcripts", "rsem-parse-alignments": "/usr/local/bin/rsem-parse-alignments", "rsem-plot-model": "/usr/local/bin/rsem-plot-model", "rsem-preref": "/usr/local/bin/rsem-preref", "rsem-sam-validator": "/usr/local/bin/rsem-sam-validator", "rsem-scan-for-paired-end-reads": "/usr/local/bin/rsem-scan-for-paired-end-reads", "rsem-simulate-reads": "/usr/local/bin/rsem-simulate-reads", "rsem-synthesis-reference-transcripts": "/usr/local/bin/rsem-synthesis-reference-transcripts", "rsem_perl_utils.pm": "/usr/local/bin/rsem_perl_utils.pm", "varfilter.py": "/usr/local/bin/varfilter.py", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "perl5.26.2": "/usr/local/bin/perl5.26.2", "ace2sam": "/usr/local/bin/ace2sam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/detonate.
shpc-registry automated BioContainers addition for detonate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/detonate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/detonate:1.11--hae1ec2f_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/detonate/1.11--hae1ec2f_3
$ module help quay.io/biocontainers/detonate/1.11--hae1ec2f_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### detonate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### detonate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### detonate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### detonate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### detonate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### detonate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ref-eval

```bash
$ singularity exec <container> /usr/local/bin/ref-eval
$ podman run --it --rm --entrypoint /usr/local/bin/ref-eval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-eval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-eval-estimate-true-assembly

```bash
$ singularity exec <container> /usr/local/bin/ref-eval-estimate-true-assembly
$ podman run --it --rm --entrypoint /usr/local/bin/ref-eval-estimate-true-assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-eval-estimate-true-assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-build-read-index

```bash
$ singularity exec <container> /usr/local/bin/rsem-build-read-index
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-build-read-index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-build-read-index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-eval-calculate-score

```bash
$ singularity exec <container> /usr/local/bin/rsem-eval-calculate-score
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-eval-calculate-score   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-eval-calculate-score   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-eval-estimate-transcript-length-distribution

```bash
$ singularity exec <container> /usr/local/bin/rsem-eval-estimate-transcript-length-distribution
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-eval-estimate-transcript-length-distribution   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-eval-estimate-transcript-length-distribution   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-eval-run-em

```bash
$ singularity exec <container> /usr/local/bin/rsem-eval-run-em
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-eval-run-em   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-eval-run-em   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-extract-reference-transcripts

```bash
$ singularity exec <container> /usr/local/bin/rsem-extract-reference-transcripts
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-extract-reference-transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-extract-reference-transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-parse-alignments

```bash
$ singularity exec <container> /usr/local/bin/rsem-parse-alignments
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-parse-alignments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-parse-alignments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-plot-model

```bash
$ singularity exec <container> /usr/local/bin/rsem-plot-model
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-plot-model   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-plot-model   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-preref

```bash
$ singularity exec <container> /usr/local/bin/rsem-preref
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-preref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-preref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-sam-validator

```bash
$ singularity exec <container> /usr/local/bin/rsem-sam-validator
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-sam-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-sam-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-scan-for-paired-end-reads

```bash
$ singularity exec <container> /usr/local/bin/rsem-scan-for-paired-end-reads
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-scan-for-paired-end-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-scan-for-paired-end-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-simulate-reads

```bash
$ singularity exec <container> /usr/local/bin/rsem-simulate-reads
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-simulate-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-simulate-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem-synthesis-reference-transcripts

```bash
$ singularity exec <container> /usr/local/bin/rsem-synthesis-reference-transcripts
$ podman run --it --rm --entrypoint /usr/local/bin/rsem-synthesis-reference-transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem-synthesis-reference-transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsem_perl_utils.pm

```bash
$ singularity exec <container> /usr/local/bin/rsem_perl_utils.pm
$ podman run --it --rm --entrypoint /usr/local/bin/rsem_perl_utils.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsem_perl_utils.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varfilter.py

```bash
$ singularity exec <container> /usr/local/bin/varfilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
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