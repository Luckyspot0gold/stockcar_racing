IEnumerator LoadDriverTexture(string textureURL) {
    using (UnityWebRequest www = UnityWebRequestTexture.GetTexture(textureURL)) {
        yield return www.SendWebRequest(); // AWAIT FIX
        
        if (www.result != UnityWebRequest.Result.Success) {
            Debug.LogError($"Texture load failed: {www.error}");
        } else {
            Texture2D texture = DownloadHandlerTexture.GetContent(www);
            GetComponent<Renderer>().material.mainTexture = texture;
        }
    }
}
