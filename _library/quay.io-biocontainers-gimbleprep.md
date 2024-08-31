---
layout: container
name:  "quay.io/biocontainers/gimbleprep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gimbleprep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gimbleprep/container.yaml"
updated_at: "2024-08-31 03:01:33.070746"
latest: "0.0.2b6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gimbleprep"
aliases:
 - "gimbleprep"
 - "mosdepth"
 - "tabix++"
 - "bc"
 - "dc"
 - "abba-baba"
 - "bFst"
 - "bed2region"
 - "bgziptabix"
 - "dumpContigsFromHeader"
 - "genotypeSummary"
 - "hapLrt"
 - "iHS"
 - "meltEHH"
 - "normalize-iHS"
 - "pFst"
 - "pVst"
 - "permuteGPAT++"
 - "permuteSmooth"
 - "plotHaps"
 - "popStats"
 - "segmentFst"
 - "segmentIhs"
 - "sequenceDiversity"
 - "smoother"
 - "vcf2bed.py"
 - "vcf2dag"
versions:
 - "0.0.2b3--pyhdfd78af_0"
 - "0.0.2b4--pyhdfd78af_0"
 - "0.0.2b5--pyhdfd78af_0"
 - "0.0.2b6--pyhdfd78af_0"
description: "singularity registry hpc automated addition for gimbleprep"
config: {"url": "https://biocontainers.pro/tools/gimbleprep", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gimbleprep", "latest": {"0.0.2b6--pyhdfd78af_0": "sha256:b5a7a13801fa11604090736de1c8b5b6ccd9015ae1c1a88ddbb3454e17cbbc78"}, "tags": {"0.0.2b3--pyhdfd78af_0": "sha256:87c695292ff937130094a5f31ed9db8fe498793f35204d9184bcab6d45dc319e", "0.0.2b4--pyhdfd78af_0": "sha256:b3c8cf5a3068110b30a067bf719a0f291a83040e16486b7fd5455f869272db86", "0.0.2b5--pyhdfd78af_0": "sha256:83886d68c572b73a2b0e682eec20f804267206f030ef9cc9f2ecd00d3780b9f3", "0.0.2b6--pyhdfd78af_0": "sha256:b5a7a13801fa11604090736de1c8b5b6ccd9015ae1c1a88ddbb3454e17cbbc78"}, "docker": "quay.io/biocontainers/gimbleprep", "aliases": {"gimbleprep": "/usr/local/bin/gimbleprep", "mosdepth": "/usr/local/bin/mosdepth", "tabix++": "/usr/local/bin/tabix++", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "abba-baba": "/usr/local/bin/abba-baba", "bFst": "/usr/local/bin/bFst", "bed2region": "/usr/local/bin/bed2region", "bgziptabix": "/usr/local/bin/bgziptabix", "dumpContigsFromHeader": "/usr/local/bin/dumpContigsFromHeader", "genotypeSummary": "/usr/local/bin/genotypeSummary", "hapLrt": "/usr/local/bin/hapLrt", "iHS": "/usr/local/bin/iHS", "meltEHH": "/usr/local/bin/meltEHH", "normalize-iHS": "/usr/local/bin/normalize-iHS", "pFst": "/usr/local/bin/pFst", "pVst": "/usr/local/bin/pVst", "permuteGPAT++": "/usr/local/bin/permuteGPAT++", "permuteSmooth": "/usr/local/bin/permuteSmooth", "plotHaps": "/usr/local/bin/plotHaps", "popStats": "/usr/local/bin/popStats", "segmentFst": "/usr/local/bin/segmentFst", "segmentIhs": "/usr/local/bin/segmentIhs", "sequenceDiversity": "/usr/local/bin/sequenceDiversity", "smoother": "/usr/local/bin/smoother", "vcf2bed.py": "/usr/local/bin/vcf2bed.py", "vcf2dag": "/usr/local/bin/vcf2dag"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gimbleprep.
singularity registry hpc automated addition for gimbleprep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gimbleprep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gimbleprep:0.0.2b6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gimbleprep/0.0.2b6--pyhdfd78af_0
$ module help quay.io/biocontainers/gimbleprep/0.0.2b6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gimbleprep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gimbleprep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gimbleprep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gimbleprep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gimbleprep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gimbleprep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gimbleprep

```bash
$ singularity exec <container> /usr/local/bin/gimbleprep
$ podman run --it --rm --entrypoint /usr/local/bin/gimbleprep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gimbleprep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mosdepth

```bash
$ singularity exec <container> /usr/local/bin/mosdepth
$ podman run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix++

```bash
$ singularity exec <container> /usr/local/bin/tabix++
$ podman run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abba-baba

```bash
$ singularity exec <container> /usr/local/bin/abba-baba
$ podman run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bFst

```bash
$ singularity exec <container> /usr/local/bin/bFst
$ podman run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bFst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed2region

```bash
$ singularity exec <container> /usr/local/bin/bed2region
$ podman run --it --rm --entrypoint /usr/local/bin/bed2region   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2region   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgziptabix

```bash
$ singularity exec <container> /usr/local/bin/bgziptabix
$ podman run --it --rm --entrypoint /usr/local/bin/bgziptabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgziptabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpContigsFromHeader

```bash
$ singularity exec <container> /usr/local/bin/dumpContigsFromHeader
$ podman run --it --rm --entrypoint /usr/local/bin/dumpContigsFromHeader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpContigsFromHeader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotypeSummary

```bash
$ singularity exec <container> /usr/local/bin/genotypeSummary
$ podman run --it --rm --entrypoint /usr/local/bin/genotypeSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotypeSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapLrt

```bash
$ singularity exec <container> /usr/local/bin/hapLrt
$ podman run --it --rm --entrypoint /usr/local/bin/hapLrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapLrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iHS

```bash
$ singularity exec <container> /usr/local/bin/iHS
$ podman run --it --rm --entrypoint /usr/local/bin/iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meltEHH

```bash
$ singularity exec <container> /usr/local/bin/meltEHH
$ podman run --it --rm --entrypoint /usr/local/bin/meltEHH   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meltEHH   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize-iHS

```bash
$ singularity exec <container> /usr/local/bin/normalize-iHS
$ podman run --it --rm --entrypoint /usr/local/bin/normalize-iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize-iHS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pFst

```bash
$ singularity exec <container> /usr/local/bin/pFst
$ podman run --it --rm --entrypoint /usr/local/bin/pFst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pFst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pVst

```bash
$ singularity exec <container> /usr/local/bin/pVst
$ podman run --it --rm --entrypoint /usr/local/bin/pVst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pVst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### permuteGPAT++

```bash
$ singularity exec <container> /usr/local/bin/permuteGPAT++
$ podman run --it --rm --entrypoint /usr/local/bin/permuteGPAT++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/permuteGPAT++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### permuteSmooth

```bash
$ singularity exec <container> /usr/local/bin/permuteSmooth
$ podman run --it --rm --entrypoint /usr/local/bin/permuteSmooth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/permuteSmooth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotHaps

```bash
$ singularity exec <container> /usr/local/bin/plotHaps
$ podman run --it --rm --entrypoint /usr/local/bin/plotHaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotHaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### popStats

```bash
$ singularity exec <container> /usr/local/bin/popStats
$ podman run --it --rm --entrypoint /usr/local/bin/popStats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/popStats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### segmentFst

```bash
$ singularity exec <container> /usr/local/bin/segmentFst
$ podman run --it --rm --entrypoint /usr/local/bin/segmentFst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segmentFst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### segmentIhs

```bash
$ singularity exec <container> /usr/local/bin/segmentIhs
$ podman run --it --rm --entrypoint /usr/local/bin/segmentIhs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segmentIhs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sequenceDiversity

```bash
$ singularity exec <container> /usr/local/bin/sequenceDiversity
$ podman run --it --rm --entrypoint /usr/local/bin/sequenceDiversity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sequenceDiversity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smoother

```bash
$ singularity exec <container> /usr/local/bin/smoother
$ podman run --it --rm --entrypoint /usr/local/bin/smoother   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smoother   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2bed.py

```bash
$ singularity exec <container> /usr/local/bin/vcf2bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2dag

```bash
$ singularity exec <container> /usr/local/bin/vcf2dag
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2dag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2dag   -v ${PWD} -w ${PWD} <container> -c " $@"
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