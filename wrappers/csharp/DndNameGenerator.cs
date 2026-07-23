using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Net.Http;
using System.Threading.Tasks;


public class DndNameGenerator
{
    private Dictionary<string, RaceData> _races;
    private string _version;
    private string _updateUrl;
    private Random _random = new Random();

    public DndNameGenerator(string jsonPath = "../data/names_database.json")
    {
        string json = File.ReadAllText(jsonPath);
        Root root = JsonSerializer.Deserialize<Root>(json);
        _races = root.Races;
        _version = root.Meta.Version;
        _updateUrl = root.Meta.UpdateUrl;
    }

    public string Generate(string race)
    {
        if (_races.ContainsKey(race))
        {
            var prefixes = _races[race].Prefixes;
            var suffixes = _races[race].Suffixes;
            var prefix = prefixes[_random.Next(prefixes.Count)];
            var suffix = suffixes[_random.Next(suffixes.Count)];
            return prefix + suffix;
        }
        return null;
    }

    public async Task<bool> CheckForUpdatesAsync()
    {
        try
        {
            using var client = new HttpClient();
            client.Timeout = TimeSpan.FromSeconds(3);

            string json = await client.GetStringAsync(_updateUrl);
            var remote = JsonSerializer.Deserialize<Root>(json);

            return remote.Meta.Version != _version;
        }
        catch
        {
            return false;
        }
    }
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
