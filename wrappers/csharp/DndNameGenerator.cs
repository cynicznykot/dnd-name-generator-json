using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;


public class DndNameGenerator
{
    private Dictionary<string, RaceData> _races;
    private string _version;

}

public class Root
{
    public Meta Meta { get; set; }
    public Dictionary<string, RaceData> Races { get; set; }

}
public class Meta
{
    public string Version { get; set; }
    public string UpdateUrl { get; set; }

}
public class RaceData
{
    public List<string> Prefixes { get; set; }
    public List<string> Suffixes { get; set; }
}
