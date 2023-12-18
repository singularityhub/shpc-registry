---
layout: container
name:  "quay.io/biocontainers/snp-pipeline"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snp-pipeline/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snp-pipeline/container.yaml"
updated_at: "2023-12-18 02:48:11.612229"
latest: "2.2.1--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/snp-pipeline"
aliases:
 - "alignSampleToReference.sh"
 - "calculate_snp_distances.py"
 - "call_consensus.py"
 - "cfsan_snp_pipeline"
 - "collectSampleMetrics.sh"
 - "combineSampleMetrics.sh"
 - "copy_snppipeline_data.py"
 - "create_snp_list.py"
 - "create_snp_matrix.py"
 - "create_snp_reference_seq.py"
 - "mergeVcf.sh"
 - "prepReference.sh"
 - "prepSamples.sh"
 - "qarrayrun"
 - "run_snp_pipeline.sh"
 - "snp_filter.py"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "2.2.1--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for snp-pipeline"
config: {"url": "https://biocontainers.pro/tools/snp-pipeline", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snp-pipeline", "latest": {"2.2.1--pyh3252c3a_0": "sha256:ea9d663b2a3137f53a584f57f711bdf66ab62e2336b5d9e21db645f4bc52d2aa"}, "tags": {"2.2.1--pyh3252c3a_0": "sha256:ea9d663b2a3137f53a584f57f711bdf66ab62e2336b5d9e21db645f4bc52d2aa"}, "docker": "quay.io/biocontainers/snp-pipeline", "aliases": {"alignSampleToReference.sh": "/usr/local/bin/alignSampleToReference.sh", "calculate_snp_distances.py": "/usr/local/bin/calculate_snp_distances.py", "call_consensus.py": "/usr/local/bin/call_consensus.py", "cfsan_snp_pipeline": "/usr/local/bin/cfsan_snp_pipeline", "collectSampleMetrics.sh": "/usr/local/bin/collectSampleMetrics.sh", "combineSampleMetrics.sh": "/usr/local/bin/combineSampleMetrics.sh", "copy_snppipeline_data.py": "/usr/local/bin/copy_snppipeline_data.py", "create_snp_list.py": "/usr/local/bin/create_snp_list.py", "create_snp_matrix.py": "/usr/local/bin/create_snp_matrix.py", "create_snp_reference_seq.py": "/usr/local/bin/create_snp_reference_seq.py", "mergeVcf.sh": "/usr/local/bin/mergeVcf.sh", "prepReference.sh": "/usr/local/bin/prepReference.sh", "prepSamples.sh": "/usr/local/bin/prepSamples.sh", "qarrayrun": "/usr/local/bin/qarrayrun", "run_snp_pipeline.sh": "/usr/local/bin/run_snp_pipeline.sh", "snp_filter.py": "/usr/local/bin/snp_filter.py", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snp-pipeline.
shpc-registry automated BioContainers addition for snp-pipeline
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snp-pipeline
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snp-pipeline:2.2.1--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snp-pipeline/2.2.1--pyh3252c3a_0
$ module help quay.io/biocontainers/snp-pipeline/2.2.1--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snp-pipeline-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snp-pipeline-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snp-pipeline-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snp-pipeline-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snp-pipeline-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snp-pipeline-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alignSampleToReference.sh

```bash
$ singularity exec <container> /usr/local/bin/alignSampleToReference.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alignSampleToReference.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignSampleToReference.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calculate_snp_distances.py

```bash
$ singularity exec <container> /usr/local/bin/calculate_snp_distances.py
$ podman run --it --rm --entrypoint /usr/local/bin/calculate_snp_distances.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculate_snp_distances.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### call_consensus.py

```bash
$ singularity exec <container> /usr/local/bin/call_consensus.py
$ podman run --it --rm --entrypoint /usr/local/bin/call_consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/call_consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfsan_snp_pipeline

```bash
$ singularity exec <container> /usr/local/bin/cfsan_snp_pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/cfsan_snp_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfsan_snp_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### collectSampleMetrics.sh

```bash
$ singularity exec <container> /usr/local/bin/collectSampleMetrics.sh
$ podman run --it --rm --entrypoint /usr/local/bin/collectSampleMetrics.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/collectSampleMetrics.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineSampleMetrics.sh

```bash
$ singularity exec <container> /usr/local/bin/combineSampleMetrics.sh
$ podman run --it --rm --entrypoint /usr/local/bin/combineSampleMetrics.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineSampleMetrics.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copy_snppipeline_data.py

```bash
$ singularity exec <container> /usr/local/bin/copy_snppipeline_data.py
$ podman run --it --rm --entrypoint /usr/local/bin/copy_snppipeline_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copy_snppipeline_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_snp_list.py

```bash
$ singularity exec <container> /usr/local/bin/create_snp_list.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_snp_list.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_snp_list.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_snp_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/create_snp_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_snp_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_snp_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_snp_reference_seq.py

```bash
$ singularity exec <container> /usr/local/bin/create_snp_reference_seq.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_snp_reference_seq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_snp_reference_seq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeVcf.sh

```bash
$ singularity exec <container> /usr/local/bin/mergeVcf.sh
$ podman run --it --rm --entrypoint /usr/local/bin/mergeVcf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeVcf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepReference.sh

```bash
$ singularity exec <container> /usr/local/bin/prepReference.sh
$ podman run --it --rm --entrypoint /usr/local/bin/prepReference.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepReference.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepSamples.sh

```bash
$ singularity exec <container> /usr/local/bin/prepSamples.sh
$ podman run --it --rm --entrypoint /usr/local/bin/prepSamples.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepSamples.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qarrayrun

```bash
$ singularity exec <container> /usr/local/bin/qarrayrun
$ podman run --it --rm --entrypoint /usr/local/bin/qarrayrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qarrayrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_snp_pipeline.sh

```bash
$ singularity exec <container> /usr/local/bin/run_snp_pipeline.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_snp_pipeline.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_snp_pipeline.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp_filter.py

```bash
$ singularity exec <container> /usr/local/bin/snp_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/snp_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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