---
layout: container
name:  "quay.io/biocontainers/pydnase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pydnase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pydnase/container.yaml"
updated_at: "2023-04-03 04:20:39.389202"
latest: "0.3.0--py37h8902056_4"
container_url: "https://biocontainers.pro/tools/pydnase"
aliases:
 - "dnase_average_profile.py"
 - "dnase_bias_estimator.py"
 - "dnase_cut_counter.py"
 - "dnase_ddhs_scorer.py"
 - "dnase_to_JSON.py"
 - "dnase_to_javatreeview.py"
 - "dnase_wig_tracks.py"
 - "example_footprint_scores.py"
 - "wellington_bootstrap.py"
 - "wellington_footprints.py"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "fasta-sanitize.pl"
 - "shiftBed"
 - "plot-ampliconstats"
 - "annotateBed"
 - "bamToBed"
versions:
 - "0.3.0--py37h8902056_4"
description: "shpc-registry automated BioContainers addition for pydnase"
config: {"url": "https://biocontainers.pro/tools/pydnase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pydnase", "latest": {"0.3.0--py37h8902056_4": "sha256:93a278a199cf75a2c4a1a733c398129f7588b16eaa43482e6ceacf861b22e058"}, "tags": {"0.3.0--py37h8902056_4": "sha256:93a278a199cf75a2c4a1a733c398129f7588b16eaa43482e6ceacf861b22e058"}, "docker": "quay.io/biocontainers/pydnase", "aliases": {"dnase_average_profile.py": "/usr/local/bin/dnase_average_profile.py", "dnase_bias_estimator.py": "/usr/local/bin/dnase_bias_estimator.py", "dnase_cut_counter.py": "/usr/local/bin/dnase_cut_counter.py", "dnase_ddhs_scorer.py": "/usr/local/bin/dnase_ddhs_scorer.py", "dnase_to_JSON.py": "/usr/local/bin/dnase_to_JSON.py", "dnase_to_javatreeview.py": "/usr/local/bin/dnase_to_javatreeview.py", "dnase_wig_tracks.py": "/usr/local/bin/dnase_wig_tracks.py", "example_footprint_scores.py": "/usr/local/bin/example_footprint_scores.py", "wellington_bootstrap.py": "/usr/local/bin/wellington_bootstrap.py", "wellington_footprints.py": "/usr/local/bin/wellington_footprints.py", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "shiftBed": "/usr/local/bin/shiftBed", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pydnase.
shpc-registry automated BioContainers addition for pydnase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pydnase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pydnase:0.3.0--py37h8902056_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pydnase/0.3.0--py37h8902056_4
$ module help quay.io/biocontainers/pydnase/0.3.0--py37h8902056_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pydnase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pydnase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pydnase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pydnase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pydnase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pydnase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnase_average_profile.py

```bash
$ singularity exec <container> /usr/local/bin/dnase_average_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/dnase_average_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnase_average_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnase_bias_estimator.py

```bash
$ singularity exec <container> /usr/local/bin/dnase_bias_estimator.py
$ podman run --it --rm --entrypoint /usr/local/bin/dnase_bias_estimator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnase_bias_estimator.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnase_cut_counter.py

```bash
$ singularity exec <container> /usr/local/bin/dnase_cut_counter.py
$ podman run --it --rm --entrypoint /usr/local/bin/dnase_cut_counter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnase_cut_counter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnase_ddhs_scorer.py

```bash
$ singularity exec <container> /usr/local/bin/dnase_ddhs_scorer.py
$ podman run --it --rm --entrypoint /usr/local/bin/dnase_ddhs_scorer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnase_ddhs_scorer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnase_to_JSON.py

```bash
$ singularity exec <container> /usr/local/bin/dnase_to_JSON.py
$ podman run --it --rm --entrypoint /usr/local/bin/dnase_to_JSON.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnase_to_JSON.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnase_to_javatreeview.py

```bash
$ singularity exec <container> /usr/local/bin/dnase_to_javatreeview.py
$ podman run --it --rm --entrypoint /usr/local/bin/dnase_to_javatreeview.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnase_to_javatreeview.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnase_wig_tracks.py

```bash
$ singularity exec <container> /usr/local/bin/dnase_wig_tracks.py
$ podman run --it --rm --entrypoint /usr/local/bin/dnase_wig_tracks.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnase_wig_tracks.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### example_footprint_scores.py

```bash
$ singularity exec <container> /usr/local/bin/example_footprint_scores.py
$ podman run --it --rm --entrypoint /usr/local/bin/example_footprint_scores.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/example_footprint_scores.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wellington_bootstrap.py

```bash
$ singularity exec <container> /usr/local/bin/wellington_bootstrap.py
$ podman run --it --rm --entrypoint /usr/local/bin/wellington_bootstrap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wellington_bootstrap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wellington_footprints.py

```bash
$ singularity exec <container> /usr/local/bin/wellington_footprints.py
$ podman run --it --rm --entrypoint /usr/local/bin/wellington_footprints.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wellington_footprints.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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