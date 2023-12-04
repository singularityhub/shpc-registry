---
layout: container
name:  "quay.io/biocontainers/inspector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/inspector/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/inspector/container.yaml"
updated_at: "2023-12-04 02:30:58.810634"
latest: "1.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/inspector"
aliases:
 - "debreak_detect.py"
 - "debreak_merge.py"
 - "debreak_merge_clustering.py"
 - "denovo_baseerror.py"
 - "denovo_correct.py"
 - "denovo_plot.py"
 - "denovo_static.py"
 - "flye"
 - "flye-minimap2"
 - "flye-modules"
 - "flye-samtools"
 - "inspector-correct.py"
 - "inspector.py"
 - "paftools.js"
 - "minimap2"
 - "f2py3.8"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "interpolate_sam.pl"
 - "maq2sam-long"
 - "maq2sam-short"
 - "md5fa"
 - "md5sum-lite"
 - "plot-bamstats"
 - "psl2sam.pl"
 - "sam2vcf.pl"
 - "samtools.pl"
 - "seq_cache_populate.pl"
 - "soap2sam.pl"
 - "zoom2sam.pl"
 - "novo2sam.pl"
 - "wgsim"
 - "wgsim_eval.pl"
 - "samtools"
 - "htsfile"
 - "bgzip"
versions:
 - "1.2--hdfd78af_0"
description: "singularity registry hpc automated addition for inspector"
config: {"url": "https://biocontainers.pro/tools/inspector", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for inspector", "latest": {"1.2--hdfd78af_0": "sha256:b507b137ab15dfedb22db4fbce7c828d74d09226ef1e2d29ecd547f1515de672"}, "tags": {"1.2--hdfd78af_0": "sha256:b507b137ab15dfedb22db4fbce7c828d74d09226ef1e2d29ecd547f1515de672"}, "docker": "quay.io/biocontainers/inspector", "aliases": {"debreak_detect.py": "/usr/local/bin/debreak_detect.py", "debreak_merge.py": "/usr/local/bin/debreak_merge.py", "debreak_merge_clustering.py": "/usr/local/bin/debreak_merge_clustering.py", "denovo_baseerror.py": "/usr/local/bin/denovo_baseerror.py", "denovo_correct.py": "/usr/local/bin/denovo_correct.py", "denovo_plot.py": "/usr/local/bin/denovo_plot.py", "denovo_static.py": "/usr/local/bin/denovo_static.py", "flye": "/usr/local/bin/flye", "flye-minimap2": "/usr/local/bin/flye-minimap2", "flye-modules": "/usr/local/bin/flye-modules", "flye-samtools": "/usr/local/bin/flye-samtools", "inspector-correct.py": "/usr/local/bin/inspector-correct.py", "inspector.py": "/usr/local/bin/inspector.py", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "f2py3.8": "/usr/local/bin/f2py3.8", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa", "md5sum-lite": "/usr/local/bin/md5sum-lite", "plot-bamstats": "/usr/local/bin/plot-bamstats", "psl2sam.pl": "/usr/local/bin/psl2sam.pl", "sam2vcf.pl": "/usr/local/bin/sam2vcf.pl", "samtools.pl": "/usr/local/bin/samtools.pl", "seq_cache_populate.pl": "/usr/local/bin/seq_cache_populate.pl", "soap2sam.pl": "/usr/local/bin/soap2sam.pl", "zoom2sam.pl": "/usr/local/bin/zoom2sam.pl", "novo2sam.pl": "/usr/local/bin/novo2sam.pl", "wgsim": "/usr/local/bin/wgsim", "wgsim_eval.pl": "/usr/local/bin/wgsim_eval.pl", "samtools": "/usr/local/bin/samtools", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/inspector.
singularity registry hpc automated addition for inspector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/inspector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/inspector:1.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/inspector/1.2--hdfd78af_0
$ module help quay.io/biocontainers/inspector/1.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### inspector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### inspector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### inspector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### inspector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### inspector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### inspector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### debreak_detect.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_detect.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_detect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_detect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_merge.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debreak_merge_clustering.py

```bash
$ singularity exec <container> /usr/local/bin/debreak_merge_clustering.py
$ podman run --it --rm --entrypoint /usr/local/bin/debreak_merge_clustering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debreak_merge_clustering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### denovo_baseerror.py

```bash
$ singularity exec <container> /usr/local/bin/denovo_baseerror.py
$ podman run --it --rm --entrypoint /usr/local/bin/denovo_baseerror.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/denovo_baseerror.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### denovo_correct.py

```bash
$ singularity exec <container> /usr/local/bin/denovo_correct.py
$ podman run --it --rm --entrypoint /usr/local/bin/denovo_correct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/denovo_correct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### denovo_plot.py

```bash
$ singularity exec <container> /usr/local/bin/denovo_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/denovo_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/denovo_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### denovo_static.py

```bash
$ singularity exec <container> /usr/local/bin/denovo_static.py
$ podman run --it --rm --entrypoint /usr/local/bin/denovo_static.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/denovo_static.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye

```bash
$ singularity exec <container> /usr/local/bin/flye
$ podman run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-minimap2

```bash
$ singularity exec <container> /usr/local/bin/flye-minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-modules

```bash
$ singularity exec <container> /usr/local/bin/flye-modules
$ podman run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-samtools

```bash
$ singularity exec <container> /usr/local/bin/flye-samtools
$ podman run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inspector-correct.py

```bash
$ singularity exec <container> /usr/local/bin/inspector-correct.py
$ podman run --it --rm --entrypoint /usr/local/bin/inspector-correct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inspector-correct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inspector.py

```bash
$ singularity exec <container> /usr/local/bin/inspector.py
$ podman run --it --rm --entrypoint /usr/local/bin/inspector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inspector.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### interpolate_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-long

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-long
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-short

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-short
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5fa

```bash
$ singularity exec <container> /usr/local/bin/md5fa
$ podman run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5sum-lite

```bash
$ singularity exec <container> /usr/local/bin/md5sum-lite
$ podman run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-bamstats

```bash
$ singularity exec <container> /usr/local/bin/plot-bamstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/psl2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2vcf.pl

```bash
$ singularity exec <container> /usr/local/bin/sam2vcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools.pl

```bash
$ singularity exec <container> /usr/local/bin/samtools.pl
$ podman run --it --rm --entrypoint /usr/local/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.pl

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soap2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/soap2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zoom2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/zoom2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/zoom2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zoom2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novo2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/novo2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/novo2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novo2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim

```bash
$ singularity exec <container> /usr/local/bin/wgsim
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim_eval.pl

```bash
$ singularity exec <container> /usr/local/bin/wgsim_eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools

```bash
$ singularity exec <container> /usr/local/bin/samtools
$ podman run --it --rm --entrypoint /usr/local/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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