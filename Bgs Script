-- Made By Archiston
local ScreenGui = Instance.new("ScreenGui")
local main = Instance.new("Frame")
local bgsgui = Instance.new("TextLabel")
local bgslua = Instance.new("TextButton")
local reedemcodes = Instance.new("TextButton")
local antiafk = Instance.new("TextButton")
local antilag = Instance.new("TextButton")
local close = Instance.new("TextButton")
local openmain = Instance.new("Frame")
local open = Instance.new("TextButton")

--Properties:

ScreenGui.Parent = game.CoreGui

main.Name = "main"
main.Parent = ScreenGui
main.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
main.Position = UDim2.new(0, 0, 0.611553788, 0)
main.Size = UDim2.new(0, 327, 0, 195)
main.Active = true
main.Draggable = true

bgsgui.Name = "bgsgui"
bgsgui.Parent = main
bgsgui.BackgroundColor3 = Color3.fromRGB(85, 255, 255)
bgsgui.Size = UDim2.new(0, 327, 0, 50)
bgsgui.Font = Enum.Font.SourceSans
bgsgui.Text = "BGS GUI"
bgsgui.TextColor3 = Color3.fromRGB(0, 0, 0)
bgsgui.TextScaled = true
bgsgui.TextSize = 14.000
bgsgui.TextWrapped = true

bgslua.Name = "bgslua"
bgslua.Parent = main
bgslua.BackgroundColor3 = Color3.fromRGB(255, 0, 255)
bgslua.Position = UDim2.new(0.0305810403, 0, 0.369230777, 0)
bgslua.Size = UDim2.new(0, 140, 0, 50)
bgslua.Font = Enum.Font.SourceSans
bgslua.Text = "BGS Lua"
bgslua.TextColor3 = Color3.fromRGB(0, 0, 0)
bgslua.TextSize = 14.000
bgslua.MouseButton1Down:connect(function()
	loadstring(game:HttpGet(("http://roguefamily.com/script/streleziaBGSbeta/script"),true))()
end)

reedemcodes.Name = "reedemcodes"
reedemcodes.Parent = main
reedemcodes.BackgroundColor3 = Color3.fromRGB(255, 0, 255)
reedemcodes.Position = UDim2.new(0.541284323, 0, 0.369230777, 0)
reedemcodes.Size = UDim2.new(0, 140, 0, 50)
reedemcodes.Font = Enum.Font.SourceSans
reedemcodes.Text = "Reedem Codes"
reedemcodes.TextColor3 = Color3.fromRGB(0, 0, 0)
reedemcodes.TextSize = 14.000
reedemcodes.MouseButton1Down:connect(function()
	_G.whitelistkey = "customer1"

	loadstring(game:HttpGet(("http://roguefamily.com/script/bgsTwitter/bgsTwitterv3"),true))()
end)

antiafk.Name = "antiafk"
antiafk.Parent = main
antiafk.BackgroundColor3 = Color3.fromRGB(255, 0, 255)
antiafk.Position = UDim2.new(0.0305810403, 0, 0.692307711, 0)
antiafk.Size = UDim2.new(0, 140, 0, 50)
antiafk.Font = Enum.Font.SourceSans
antiafk.Text = "Anti AFK"
antiafk.TextColor3 = Color3.fromRGB(0, 0, 0)
antiafk.TextSize = 14.000
antiafk.MouseButton1Down:connect(function()
	wait(0.5)local ba=Instance.new("ScreenGui")
	local ca=Instance.new("TextLabel")local da=Instance.new("Frame")
	local _b=Instance.new("TextLabel")local ab=Instance.new("TextLabel")ba.Parent=game.CoreGui
	ba.ZIndexBehavior=Enum.ZIndexBehavior.Sibling;ca.Parent=ba;ca.Active=true
	ca.BackgroundColor3=Color3.new(0.176471,0.176471,0.176471)ca.Draggable=true
	ca.Position=UDim2.new(0.698610067,0,0.098096624,0)ca.Size=UDim2.new(0,370,0,52)
	ca.Font=Enum.Font.SourceSansSemibold;ca.Text="Anti AFK Script"ca.TextColor3=Color3.new(0,1,1)
	ca.TextSize=22;da.Parent=ca
	da.BackgroundColor3=Color3.new(0.196078,0.196078,0.196078)da.Position=UDim2.new(0,0,1.0192306,0)
	da.Size=UDim2.new(0,370,0,107)_b.Parent=da
	_b.BackgroundColor3=Color3.new(0.176471,0.176471,0.176471)_b.Position=UDim2.new(0,0,0.800455689,0)
	_b.Size=UDim2.new(0,370,0,21)_b.Font=Enum.Font.Arial;_b.Text="Made by Dynamic. (please subscribe)"
	_b.TextColor3=Color3.new(0,1,1)_b.TextSize=20;ab.Parent=da
	ab.BackgroundColor3=Color3.new(0.176471,0.176471,0.176471)ab.Position=UDim2.new(0,0,0.158377,0)
	ab.Size=UDim2.new(0,370,0,44)ab.Font=Enum.Font.ArialBold;ab.Text="Status: Active"
	ab.TextColor3=Color3.new(0,1,1)ab.TextSize=20;local bb=game:service'VirtualUser'
	game:service'Players'.LocalPlayer.Idled:connect(function()
		bb:CaptureController()bb:ClickButton2(Vector2.new())
		ab.Text="Roblox Tried to kick you but we didnt let them kick you :D"wait(2)ab.Text="Status : Active"end)
end)

antilag.Name = "antilag"
antilag.Parent = main
antilag.BackgroundColor3 = Color3.fromRGB(255, 0, 255)
antilag.Position = UDim2.new(0.544342399, 0, 0.692307711, 0)
antilag.Size = UDim2.new(0, 139, 0, 50)
antilag.Font = Enum.Font.SourceSans
antilag.Text = "Anti LAG"
antilag.TextColor3 = Color3.fromRGB(0, 0, 0)
antilag.TextSize = 14.000
antilag.MouseButton1Down:connect(function()
	local decalsyeeted = true -- Leaving this on makes games look shitty but the fps goes up by at least 20.
	local g = game
	local w = g.Workspace
	local l = g.Lighting
	local t = w.Terrain
	t.WaterWaveSize = 0
	t.WaterWaveSpeed = 0
	t.WaterReflectance = 0
	t.WaterTransparency = 0
	l.GlobalShadows = false
	l.FogEnd = 9e9
	l.Brightness = 0
	settings().Rendering.QualityLevel = "Level01"
	for i, v in pairs(g:GetDescendants()) do
		if v:IsA("Part") or v:IsA("Union") or v:IsA("CornerWedgePart") or v:IsA("TrussPart") then
			v.Material = "Plastic"
			v.Reflectance = 0
		elseif v:IsA("Decal") or v:IsA("Texture") and decalsyeeted then
			v.Transparency = 1
		elseif v:IsA("ParticleEmitter") or v:IsA("Trail") then
			v.Lifetime = NumberRange.new(0)
		elseif v:IsA("Explosion") then
			v.BlastPressure = 1
			v.BlastRadius = 1
		elseif v:IsA("Fire") or v:IsA("SpotLight") or v:IsA("Smoke") then
			v.Enabled = false
		elseif v:IsA("MeshPart") then
			v.Material = "Plastic"
			v.Reflectance = 0
			v.TextureID = 10385902758728957
		end
	end
	for i, e in pairs(l:GetChildren()) do
		if e:IsA("BlurEffect") or e:IsA("SunRaysEffect") or e:IsA("ColorCorrectionEffect") or e:IsA("BloomEffect") or e:IsA("DepthOfFieldEffect") then
			e.Enabled = false
		end
	end
end)
